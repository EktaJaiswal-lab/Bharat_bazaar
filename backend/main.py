from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import client

app = FastAPI(
    title="Bharat Bazaar API",
    description="Backend API for the Bharat Bazaar E-commerce platform",
    version="1.0.0"
)

# Configure CORS
origins = [
    "http://localhost:5173", # Vite default
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes import auth, product, interaction, chat, analytics
from ml.recommendation import recommendation_engine
import asyncio

@app.on_event("startup")
async def startup_db_client():
    print("Connected to the MongoDB database!")
    print("Training Recommendation Engine...")
    asyncio.create_task(recommendation_engine.train())

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
    print("Disconnected from the MongoDB database!")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(product.router, prefix="/products", tags=["products"])
app.include_router(interaction.router, prefix="/interactions", tags=["interactions"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Bharat Bazaar API"}
