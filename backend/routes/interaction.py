from fastapi import APIRouter, Depends, HTTPException
from typing import List
from database import get_database
from models.interaction import InteractionCreate, InteractionInDB, InteractionOut
from routes.auth import get_current_user
from models.user import UserInDB
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/", response_model=InteractionOut)
async def record_interaction(
    interaction: InteractionCreate,
    db = Depends(get_database),
    current_user: UserInDB = Depends(get_current_user)
):
    # Ensure user is creating interaction for themselves
    if interaction.user_id != str(current_user.id):
        raise HTTPException(status_code=403, detail="Not authorized to record interactions for another user")
        
    # Check if product exists
    product = await db["products"].find_one({"_id": interaction.product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    # Special handling for wishlist and rating to prevent duplicates/updates
    if interaction.interaction_type in ["wishlist", "rate"]:
        existing = await db["interactions"].find_one({
            "user_id": interaction.user_id,
            "product_id": interaction.product_id,
            "interaction_type": interaction.interaction_type
        })
        if existing:
            # Update existing
            await db["interactions"].update_one(
                {"_id": existing["_id"]},
                {"$set": {
                    "rating_value": interaction.rating_value,
                    "timestamp": datetime.utcnow()
                }}
            )
            updated = await db["interactions"].find_one({"_id": existing["_id"]})
            return updated
            
    # Create new interaction
    interaction_dict = interaction.dict()
    interaction_dict["_id"] = str(uuid.uuid4())
    interaction_dict["timestamp"] = datetime.utcnow()
    
    await db["interactions"].insert_one(interaction_dict)
    
    return interaction_dict

@router.get("/wishlist", response_model=List[InteractionOut])
async def get_wishlist(
    db = Depends(get_database),
    current_user: UserInDB = Depends(get_current_user)
):
    cursor = db["interactions"].find({
        "user_id": str(current_user.id),
        "interaction_type": "wishlist"
    }).sort("timestamp", -1)
    
    wishlist = await cursor.to_list(length=100)
    return wishlist

@router.delete("/wishlist/{product_id}")
async def remove_from_wishlist(
    product_id: str,
    db = Depends(get_database),
    current_user: UserInDB = Depends(get_current_user)
):
    result = await db["interactions"].delete_one({
        "user_id": str(current_user.id),
        "product_id": product_id,
        "interaction_type": "wishlist"
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found in wishlist")
        
    return {"message": "Removed from wishlist"}
