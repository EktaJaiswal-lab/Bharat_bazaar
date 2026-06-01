import os
import re
import random
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Static FAQ Database for Bharat Bazaar
LOCAL_FAQ = [
    {
        "keywords": ["hi", "hello", "hey", "greetings", "anyone there", "yo", "sup"],
        "questions": ["hi", "hello", "hey", "is anyone there", "hello assistant", "good morning", "good afternoon"],
        "answer": "Hello! Welcome to Bharat Bazaar. I am your AI-powered shopping assistant. How can I help you today?"
    },
    {
        "keywords": ["return", "refund", "exchange", "policy", "days", "back", "cancel"],
        "questions": [
            "what is the return policy?", 
            "how to return an item?", 
            "can i get a refund?", 
            "is there a return policy?", 
            "how many days do i have to return an item?",
            "refund policy",
            "return items"
        ],
        "answer": "We offer a **30-day hassle-free return policy** on all items! If you're not completely satisfied, you can return your purchase in its original condition and packaging within 30 days of delivery for a full refund or exchange."
    },
    {
        "keywords": ["shipping", "delivery", "charge", "cost", "how long", "time", "days", "arrive", "fee"],
        "questions": [
            "what are the shipping charges?", 
            "how long does delivery take?", 
            "do you have free shipping?", 
            "when will my order arrive?",
            "what is the delivery time?",
            "shipping cost",
            "delivery charges"
        ],
        "answer": "Standard shipping takes **3-5 business days** across India. We offer **free shipping** on all orders above ₹499! For orders below ₹499, a flat shipping fee of ₹50 applies."
    },
    {
        "keywords": ["payment", "pay", "cod", "upi", "card", "credit", "debit", "gpay", "phonepe", "cash"],
        "questions": [
            "what payment methods do you support?", 
            "can i pay with cash on delivery?", 
            "do you accept upi?", 
            "how do i pay for my order?",
            "is cash on delivery available?",
            "payment options"
        ],
        "answer": "We support a wide range of secure payment methods, including all major **Credit/Debit Cards, UPI (GPay, PhonePe, Paytm), Net Banking**, and **Cash on Delivery (COD)** for eligible pin codes."
    },
    {
        "keywords": ["track", "order", "status", "where is my", "shipped", "tracking", "package"],
        "questions": [
            "how do i track my order?", 
            "where is my order?", 
            "can i see my order status?", 
            "how to track package?",
            "order tracking"
        ],
        "answer": "Once your order is shipped, you will receive an SMS and email containing a **tracking link**. You can also check your real-time order status by heading to the **'Orders'** section of your profile dashboard!"
    },
    {
        "keywords": ["contact", "support", "customer", "care", "email", "phone", "help", "talk", "number", "call"],
        "questions": [
            "how do i contact customer care?", 
            "who can i talk to for help?", 
            "what is your email address?", 
            "what is your customer support phone number?",
            "customer care phone number"
        ],
        "answer": "Our customer support team is happy to help! You can reach us via email at **support@bharatbazaar.com** or call our toll-free customer care number at **1800-123-4567** (available 24/7)."
    },
    {
        "keywords": ["discount", "coupon", "promo", "code", "offer", "sale", "welcome", "cheap"],
        "questions": [
            "are there any discount codes?", 
            "do you have active coupons?", 
            "how to get a promo code?", 
            "any discount for first purchase?",
            "promo codes",
            "coupons"
        ],
        "answer": "Yes! You can use the promo code **WELCOME10** at checkout to get an instant **10% discount** on your first purchase. Keep an eye on our homepage for seasonal sales and exclusive offers!"
    },
    {
        "keywords": ["product", "category", "sell", "items", "what do you", "categories", "store"],
        "questions": [
            "what categories of products do you have?", 
            "what do you sell?", 
            "what kinds of items are available?", 
            "tell me about your product categories",
            "product categories"
        ],
        "answer": "Bharat Bazaar offers premium products across 10 major categories:\n- **Electronics** & **Wearables**\n- **Fashion** & **Beauty**\n- **Home & Living** & **Kitchen**\n- **Gaming** & **Sports**\n- **Wellness** & **Books**\n\nExplore our homepage to view the curated collections!"
    },
    {
        "keywords": ["about", "bharat", "bazaar", "store", "company", "who are you", "what is this"],
        "questions": [
            "what is bharat bazaar?", 
            "tell me about bharat bazaar", 
            "what is this store about?",
            "who are you"
        ],
        "answer": "Bharat Bazaar is a next-generation, premium AI-powered e-commerce platform. We curate the finest quality products ranging from electronics to fashion, providing an intelligent, personalized, and seamless shopping experience powered by advanced recommendation engines."
    }
]

# Robust fallback answers if no specific FAQ category matches
DEFAULT_FALLBACKS = [
    "I'm here to help! Although my main AI brain is experiencing a temporary connection issue, I can answer questions about our return policy, shipping, order tracking, payment methods, or contact information. What can I help you with?",
    "My AI core is currently performing maintenance, but I can guide you through our standard policies. Ask me about returns, delivery times, shipping costs, payment options, or how to contact our customer care team!",
    "It seems I'm offline from my main neural net, but I have my local database active! I can answer questions about shipping, standard 30-day returns, accepted payments, coupon codes, and store contact info. Feel free to ask!"
]

class ChatbotEngine:
    def __init__(self):
        self.client = None
        self.model = "gemini-2.0-flash"
        self.is_configured = False
        
        # Try initial configuration
        if GEMINI_API_KEY:
            self.client = genai.Client(api_key=GEMINI_API_KEY)
            self.is_configured = True
        else:
            print("WARNING: GEMINI_API_KEY not found in environment. Chatbot will be disabled until configured.")

        self.system_prompt = """
You are the Bharat Bazaar AI Assistant, a helpful, futuristic, and premium customer support agent for an AI-powered e-commerce platform called 'Bharat Bazaar'.
Your goals are to:
1. Help customers find products.
2. Answer questions about the store's return policy (30-day hassle-free returns on all items).
3. Provide recommendations based on their queries.
4. Maintain a polite, concise, and slightly futuristic/tech-savvy tone.

Keep your responses short and formatting clean using Markdown if needed. Do not make up product prices or features unless giving a hypothetical example.
"""

    def clean_and_tokenize(self, text: str) -> set:
        if not text:
            return set()
        # Remove punctuation and lowercase
        cleaned = re.sub(r'[^\w\s]', '', text.lower())
        return set(cleaned.split())

    def find_best_local_match(self, message: str):
        query_tokens = self.clean_and_tokenize(message)
        if not query_tokens:
            return None, 0.0

        best_answer = None
        best_score = 0.0

        for faq in LOCAL_FAQ:
            category_best_q_score = 0.0
            for question in faq["questions"]:
                question_tokens = self.clean_and_tokenize(question)
                
                # Jaccard similarity
                intersection = query_tokens.intersection(question_tokens)
                union = query_tokens.union(question_tokens)
                jaccard = len(intersection) / len(union) if union else 0.0
                
                # Substring match bonus
                cleaned_q = question.lower()
                cleaned_query = message.lower()
                if cleaned_q in cleaned_query or cleaned_query in cleaned_q:
                    jaccard = max(jaccard, 0.6)
                    
                if jaccard > category_best_q_score:
                    category_best_q_score = jaccard

            # Keyword matching bonus
            keyword_matches = sum(1 for kw in faq["keywords"] if kw in message.lower())
            keyword_bonus = 0.0
            if keyword_matches > 0:
                keyword_bonus = min(0.25, keyword_matches * 0.1)

            final_score = category_best_q_score + keyword_bonus
            
            # Exact keyword match for very short queries (1-2 words)
            if len(query_tokens) <= 2:
                for kw in faq["keywords"]:
                    if kw in query_tokens:
                        final_score = max(final_score, 0.7)

            if final_score > best_score:
                best_score = final_score
                best_answer = faq["answer"]

        return best_answer, best_score

    async def get_response(self, message: str, history: list = None):
        # 1. Primary Match: check for a high-confidence local Q&A match (score >= 0.55)
        # This gives instantaneous answers for FAQs without making API calls.
        local_answer, similarity_score = self.find_best_local_match(message)
        if local_answer and similarity_score >= 0.55:
            print(f"Chatbot: Serving high-confidence local FAQ match (score: {similarity_score:.2f})")
            return local_answer

        # 2. Try Gemini API
        if self.is_configured:
            try:
                contents = []

                if history:
                    for msg in history:
                        role = "user" if msg["role"] == "user" else "model"
                        contents.append(types.Content(role=role, parts=[types.Part(text=msg["content"])]))

                contents.append(types.Content(role="user", parts=[types.Part(text=message)]))

                response = self.client.models.generate_content(
                    model=self.model,
                    contents=contents,
                    config=types.GenerateContentConfig(system_instruction=self.system_prompt)
                )
                return response.text

            except Exception as e:
                print(f"Chatbot Gemini Error: {e}")
                # Seamless fallback will trigger below instead of throwing an error
        else:
            # Attempt dynamic loading of the API key from .env in case it was updated
            load_dotenv()
            dynamic_key = os.getenv("GEMINI_API_KEY")
            if dynamic_key:
                try:
                    self.client = genai.Client(api_key=dynamic_key)
                    self.is_configured = True
                    # Try calling recursively with newly configured client
                    return await self.get_response(message, history)
                except Exception as e:
                    print(f"Error configuring dynamic Gemini client: {e}")

        # 3. Graceful Fallback: If Gemini failed or is offline, check for a lower-confidence local match (score >= 0.25)
        if local_answer and similarity_score >= 0.25:
            print(f"Chatbot Fallback: Serving medium-confidence local FAQ match (score: {similarity_score:.2f})")
            return local_answer

        # 4. Ultimate Fallback: Return a random supportive default response
        return random.choice(DEFAULT_FALLBACKS)

chatbot_engine = ChatbotEngine()

