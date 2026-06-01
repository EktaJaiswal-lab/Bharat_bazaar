from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
import uuid
from datetime import datetime
from database import get_database
from models.product import ProductInDB, ProductOut, ProductCreate
from ml.recommendation import recommendation_engine

router = APIRouter()

@router.get("/", response_model=List[ProductOut])
async def get_products(
    skip: int = 0, limit: int = 20, 
    category: str = None, 
    db = Depends(get_database)
):
    query = {}
    if category:
        query["category"] = category
        
    cursor = db["products"].find(query).skip(skip).limit(limit)
    products = await cursor.to_list(length=limit)
    return products

@router.post("/", response_model=ProductOut)
async def create_product(product: ProductCreate, db = Depends(get_database)):
    new_product = ProductInDB(
        _id=str(uuid.uuid4()),
        created_at=datetime.utcnow(),
        **product.dict()
    )
    await db["products"].insert_one(new_product.dict(by_alias=True))
    return new_product

@router.get("/search/", response_model=List[ProductOut])
async def search_products(q: str = Query(..., min_length=1), db = Depends(get_database)):
    results = recommendation_engine.smart_search(q, num_results=10)
    if not results:
        query = {
            "$or": [
                {"title": {"$regex": q, "$options": "i"}},
                {"category": {"$regex": q, "$options": "i"}},
                {"tags": {"$regex": q, "$options": "i"}}
            ]
        }
        cursor = db["products"].find(query).limit(20)
        results = await cursor.to_list(length=20)
    return results

@router.get("/{product_id}/similar", response_model=List[ProductOut])
async def get_similar_products(product_id: str, limit: int = 4, db = Depends(get_database)):
    """Content-based similar products"""
    recommendations = recommendation_engine.get_similar_products(product_id, num_recommendations=limit)
    return recommendations

@router.get("/recommendations/personalized", response_model=List[ProductOut])
async def get_personalized_recommendations(user_id: str = Query(...), limit: int = 10, db = Depends(get_database)):
    """Hybrid personalized recommendations based on user history"""
    recommendations = recommendation_engine.get_personalized_recommendations(user_id, num_recommendations=limit)
    return recommendations

@router.get("/{product_id}", response_model=ProductOut)
async def get_product(product_id: str, db = Depends(get_database)):
    product = await db["products"].find_one({"_id": product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
