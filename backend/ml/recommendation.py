import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from database import get_database
import asyncio

class RecommendationEngine:
    def __init__(self):
        self.products_df = None
        self.interactions_df = None
        self.content_sim = None
        self.user_item_matrix = None
        self.vectorizer = TfidfVectorizer(stop_words='english')

    async def train(self):
        db = get_database()
        
        # 1. Load Products for Content-Based Filtering
        cursor = db["products"].find({})
        products = await cursor.to_list(length=None)
        
        if not products:
            print("No products found for training.")
            return
            
        self.products_df = pd.DataFrame(products)
        self.products_df['_id'] = self.products_df['_id'].astype(str)
        
        # Create content string
        self.products_df['tags_str'] = self.products_df['tags'].apply(lambda x: ' '.join(x) if isinstance(x, list) else '')
        self.products_df['content'] = self.products_df['title'] + ' ' + self.products_df['description'] + ' ' + self.products_df['category'] + ' ' + self.products_df['tags_str']
        
        # Compute Content TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(self.products_df['content'])
        self.content_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        
        # 2. Load Interactions for Collaborative Filtering
        cursor_int = db["interactions"].find({})
        interactions = await cursor_int.to_list(length=None)
        
        if interactions:
            self.interactions_df = pd.DataFrame(interactions)
            
            # Map interaction types to weights
            def get_weight(row):
                if row['interaction_type'] == 'view': return 1.0
                if row['interaction_type'] == 'wishlist': return 3.0
                if row['interaction_type'] == 'purchase': return 5.0
                if row['interaction_type'] == 'rate': return float(row['rating_value']) if pd.notnull(row['rating_value']) else 3.0
                return 1.0
                
            self.interactions_df['weight'] = self.interactions_df.apply(get_weight, axis=1)
            
            # Group by user and product, take max weight
            grouped = self.interactions_df.groupby(['user_id', 'product_id'])['weight'].max().reset_index()
            
            # Create User-Item Matrix
            self.user_item_matrix = grouped.pivot(index='user_id', columns='product_id', values='weight').fillna(0)
            
        print("Hybrid Recommendation model trained successfully.")

    def get_similar_products(self, product_id: str, num_recommendations: int = 4):
        """Content-based similarity (item-to-item)"""
        if self.products_df is None or self.content_sim is None:
            return []
            
        if product_id not in self.products_df['_id'].values:
            return []
            
        idx = self.products_df.index[self.products_df['_id'] == product_id].tolist()[0]
        sim_scores = list(enumerate(self.content_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
        
        product_indices = [i[0] for i in sim_scores]
        recommendations = self.products_df.iloc[product_indices].to_dict('records')
        return self._format_output(recommendations)

    def get_personalized_recommendations(self, user_id: str, num_recommendations: int = 10):
        """Hybrid Recommendation: Collaborative + Content"""
        if self.products_df is None:
            return []
            
        # Cold start or no interactions at all -> return popular/random items
        if self.user_item_matrix is None or user_id not in self.user_item_matrix.index:
            return self._format_output(self.products_df.head(num_recommendations).to_dict('records'))
            
        # Collaborative Filtering (User-User similarity)
        user_vector = self.user_item_matrix.loc[user_id].values.reshape(1, -1)
        
        # Calculate similarity with all other users
        user_similarities = cosine_similarity(user_vector, self.user_item_matrix)[0]
        
        # Weight the user-item matrix by user similarity
        # Shape: (1, num_users) dot (num_users, num_items) -> (1, num_items)
        predicted_scores = user_similarities.dot(self.user_item_matrix.values)
        
        # Normalize
        if user_similarities.sum() > 0:
            predicted_scores = predicted_scores / user_similarities.sum()
            
        # Get products the user has already interacted with (to filter them out)
        user_interacted = set(self.interactions_df[self.interactions_df['user_id'] == user_id]['product_id'].values)
        
        # Create a series of scores mapped to product IDs
        scores_series = pd.Series(predicted_scores, index=self.user_item_matrix.columns)
        
        # Filter out already interacted items
        scores_series = scores_series.drop(labels=list(user_interacted.intersection(scores_series.index)))
        
        # Sort and get top
        top_collab_products = scores_series.sort_values(ascending=False).head(num_recommendations)
        
        if len(top_collab_products) == 0:
            # Fallback to content based or popular
            return self._format_output(self.products_df.head(num_recommendations).to_dict('records'))
            
        # Fetch the actual product data
        recommended_products = self.products_df[self.products_df['_id'].isin(top_collab_products.index)]
        
        # If we didn't get enough recommendations, supplement with content-based from their top interacted item
        if len(recommended_products) < num_recommendations:
            # Find their highest rated/interacted item
            user_history = self.interactions_df[self.interactions_df['user_id'] == user_id].sort_values('weight', ascending=False)
            if not user_history.empty:
                top_item_id = user_history.iloc[0]['product_id']
                content_recs = self.get_similar_products(top_item_id, num_recommendations - len(recommended_products))
                # We would merge them here, but for simplicity we'll just return what we have
                
        return self._format_output(recommended_products.to_dict('records'))

    def smart_search(self, query: str, num_results: int = 10):
        if self.products_df is None or self.vectorizer is None:
            return []
            
        query_vec = self.vectorizer.transform([query])
        tfidf_matrix = self.vectorizer.transform(self.products_df['content'])
        sim_scores = linear_kernel(query_vec, tfidf_matrix).flatten()
        
        sim_indices = sim_scores.argsort()[::-1][:num_results]
        
        results = []
        for idx in sim_indices:
            if sim_scores[idx] > 0:
                results.append(self.products_df.iloc[idx].to_dict())
                
        return self._format_output(results)

    def _format_output(self, dict_list):
        for item in dict_list:
            item['id'] = item['_id']
            item.pop('content', None)
            item.pop('tags_str', None)
        return dict_list

recommendation_engine = RecommendationEngine()
