import asyncio
import uuid
from datetime import datetime
from database import get_database, client

async def seed_data():
    db = get_database()
    
    # Drop existing collections to ensure fresh data and IDs
    await db["products"].drop()
    await db["interactions"].drop()
    print("Dropped old collections.")

    products = [
        # Electronics
        {
            "_id": str(uuid.uuid4()),
            "title": "Neon Gaming Headphones",
            "description": "High fidelity audio with futuristic neon lighting. Features 7.1 surround sound and neural-link interface.",
            "price": 7199.00,
            "category": "Electronics",
            "tags": ["gaming", "audio", "neon"],
            "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&w=500&q=80",
            "stock": 100,
            "rating": 4.5,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Quantum Mechanical Keyboard",
            "description": "Tactile feedback with reactive RGB backlighting. Zero-latency quantum switches for pro gamers.",
            "price": 11960.00,
            "category": "Electronics",
            "tags": ["gaming", "keyboard", "rgb"],
            "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=500&q=80",
            "stock": 75,
            "rating": 4.7,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Holo-Lens AR Glasses",
            "description": "Experience the world with augmented reality overlays. See navigation, messages, and calls right in your field of view.",
            "price": 39920.00,
            "category": "Electronics",
            "tags": ["ar", "glasses", "future"],
            "image_url": "https://images.unsplash.com/photo-1535223289827-42f1e9919769?auto=format&fit=crop&w=500&q=80",
            "stock": 20,
            "rating": 4.2,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Cyber-Deck Laptop",
            "description": "A portable powerhouse with a transparent OLED screen and holographic projection capabilities.",
            "price": 151999.00,
            "category": "Electronics",
            "tags": ["laptop", "cyberpunk", "computer"],
            "image_url": "https://images.unsplash.com/photo-1531297172864-dd6b18c64115?auto=format&fit=crop&w=500&q=80",
            "stock": 15,
            "rating": 4.9,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Drone Companion Pod",
            "description": "Your personal AI drone that follows you, takes photos, and carries small items.",
            "price": 27920.00,
            "category": "Electronics",
            "tags": ["drone", "ai", "camera"],
            "image_url": "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?auto=format&fit=crop&w=500&q=80",
            "stock": 45,
            "rating": 4.6,
            "created_at": datetime.utcnow()
        },
        # Wearables / Fashion
        {
            "_id": str(uuid.uuid4()),
            "title": "Cyberpunk Smartwatch",
            "description": "Advanced health tracking with a holographic UI feel. Monitors blood-oxygen, stress, and syncs directly to your neural-chip.",
            "price": 15999.00,
            "category": "Wearables",
            "tags": ["smartwatch", "health", "cyberpunk"],
            "image_url": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&w=500&q=80",
            "stock": 50,
            "rating": 4.8,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Aero-Glide Hover Sneakers",
            "description": "Ultra-lightweight footwear with magnetic lift technology. Literally walk on air.",
            "price": 20000.00,
            "category": "Fashion",
            "tags": ["shoes", "fashion", "hover"],
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80",
            "stock": 200,
            "rating": 4.9,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "LED Fiber-Optic Jacket",
            "description": "A smart jacket that changes color based on your mood and the music you are listening to.",
            "price": 10000.00,
            "category": "Fashion",
            "tags": ["jacket", "led", "clothing"],
            "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=500&q=80",
            "stock": 120,
            "rating": 4.3,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Thermo-Regulating Beanie",
            "description": "Never be too hot or too cold. This beanie automatically adjusts to your body temperature.",
            "price": 2800.00,
            "category": "Fashion",
            "tags": ["hat", "winter", "smart"],
            "image_url": "https://images.unsplash.com/photo-1576871337622-98d48d1cf531?auto=format&fit=crop&w=500&q=80",
            "stock": 300,
            "rating": 4.1,
            "created_at": datetime.utcnow()
        },
        # Home & Living
        {
            "_id": str(uuid.uuid4()),
            "title": "Levitating Planter",
            "description": "A beautiful oak-finished planter that magnetically levitates above its base. Perfect for bonsai or succulents.",
            "price": 7120.00,
            "category": "Home",
            "tags": ["decor", "plants", "levitating"],
            "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?auto=format&fit=crop&w=500&q=80",
            "stock": 80,
            "rating": 4.7,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Smart Infinity Mirror",
            "description": "Displays the time, weather, and your schedule within an endless optical illusion.",
            "price": 16800.00,
            "category": "Home",
            "tags": ["mirror", "smart home", "decor"],
            "image_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=500&q=80",
            "stock": 25,
            "rating": 4.8,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Nano-Leaf Light Panels",
            "description": "Modular lighting panels that react to touch and sync with your PC gaming setup.",
            "price": 15999.00,
            "category": "Home",
            "tags": ["lights", "rgb", "decor"],
            "image_url": "https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?auto=format&fit=crop&w=500&q=80",
            "stock": 150,
            "rating": 4.9,
            "created_at": datetime.utcnow()
        },
        # Beauty & Wellness
        {
            "_id": str(uuid.uuid4()),
            "title": "AI Skin Analyzer",
            "description": "Scans your skin at a microscopic level and formulates the perfect daily serum blend.",
            "price": 10320.00,
            "category": "Beauty",
            "tags": ["skincare", "health", "ai"],
            "image_url": "https://images.unsplash.com/photo-1596462502278-27bf85033e5a?auto=format&fit=crop&w=500&q=80",
            "stock": 60,
            "rating": 4.6,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Sonic Facial Massager",
            "description": "Uses ultrasonic vibrations to deeply clean pores and lift facial muscles.",
            "price": 3600.00,
            "category": "Beauty",
            "tags": ["skincare", "tool", "massage"],
            "image_url": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=500&q=80",
            "stock": 200,
            "rating": 4.4,
            "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()),
            "title": "Quantum Sleep Pod",
            "description": "A sensory deprivation tent for your bed that induces deep REM sleep using binaural beats.",
            "price": 68000.00,
            "category": "Wellness",
            "tags": ["sleep", "health", "bed"],
            "image_url": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=500&q=80",
            "stock": 10,
            "rating": 4.9,
            "created_at": datetime.utcnow()
        }
    ]
    
    await db["products"].insert_many(products)
    print(f"Database seeded with {len(products)} futuristic products across multiple categories!")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_data())
