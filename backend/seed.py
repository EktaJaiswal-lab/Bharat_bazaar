import asyncio
import uuid
from datetime import datetime
from database import get_database, client

async def seed_data():
    db = get_database()

    await db["products"].drop()
    await db["interactions"].drop()
    print("Dropped old collections.")

    products = [
        # ── Electronics (15) ──────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Neon Gaming Headphones",
            "description": "High fidelity 7.1 surround sound with futuristic neon RGB lighting.",
            "price": 7199.00, "category": "Electronics", "tags": ["gaming", "audio", "neon"],
            "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?auto=format&fit=crop&w=500&q=80",
            "stock": 100, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Quantum Mechanical Keyboard",
            "description": "Tactile RGB keyboard with zero-latency quantum switches for pro gamers.",
            "price": 11960.00, "category": "Electronics", "tags": ["gaming", "keyboard", "rgb"],
            "image_url": "https://images.unsplash.com/photo-1595225476474-87563907a212?auto=format&fit=crop&w=500&q=80",
            "stock": 75, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Holo-Lens AR Glasses",
            "description": "See navigation, messages, and calls right in your field of view.",
            "price": 39920.00, "category": "Electronics", "tags": ["ar", "glasses", "future"],
            "image_url": "https://images.unsplash.com/photo-1535223289827-42f1e9919769?auto=format&fit=crop&w=500&q=80",
            "stock": 20, "rating": 4.2, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Cyber-Deck Laptop",
            "description": "Portable powerhouse with transparent OLED screen and holographic projection.",
            "price": 151999.00, "category": "Electronics", "tags": ["laptop", "cyberpunk", "computer"],
            "image_url": "https://images.unsplash.com/photo-1531297172864-dd6b18c64115?auto=format&fit=crop&w=500&q=80",
            "stock": 15, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Drone Companion Pod",
            "description": "Personal AI drone that follows you, takes photos, and carries small items.",
            "price": 27920.00, "category": "Electronics", "tags": ["drone", "ai", "camera"],
            "image_url": "https://images.unsplash.com/photo-1507582020474-9a35b7d455d9?auto=format&fit=crop&w=500&q=80",
            "stock": 45, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "4K Ultra OLED Monitor",
            "description": "27-inch 4K OLED display with 144Hz refresh rate and HDR10+ support.",
            "price": 49999.00, "category": "Electronics", "tags": ["monitor", "4k", "oled"],
            "image_url": "https://images.unsplash.com/photo-1593640408182-31c228b6e585?auto=format&fit=crop&w=500&q=80",
            "stock": 30, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Wireless Noise-Cancel Earbuds",
            "description": "Active noise cancellation with 30hr battery and spatial audio.",
            "price": 8999.00, "category": "Electronics", "tags": ["earbuds", "audio", "wireless"],
            "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Smart Bluetooth Speaker",
            "description": "360-degree sound with built-in voice assistant and LED mood lighting.",
            "price": 5499.00, "category": "Electronics", "tags": ["speaker", "bluetooth", "smart"],
            "image_url": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=500&q=80",
            "stock": 150, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Mirrorless Camera Pro",
            "description": "50MP full-frame mirrorless camera with AI autofocus and 8K video.",
            "price": 189999.00, "category": "Electronics", "tags": ["camera", "photography", "4k"],
            "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=500&q=80",
            "stock": 10, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Smart Home Hub",
            "description": "Control all your IoT devices from one sleek central hub with voice control.",
            "price": 6999.00, "category": "Electronics", "tags": ["smart home", "iot", "hub"],
            "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=500&q=80",
            "stock": 80, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Foldable Smartphone",
            "description": "Revolutionary foldable display smartphone with dual-screen productivity mode.",
            "price": 119999.00, "category": "Electronics", "tags": ["phone", "foldable", "smartphone"],
            "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=500&q=80",
            "stock": 25, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Portable SSD 2TB",
            "description": "Ultra-fast 2000MB/s read speed portable SSD with military-grade protection.",
            "price": 12999.00, "category": "Electronics", "tags": ["storage", "ssd", "portable"],
            "image_url": "https://images.unsplash.com/photo-1597852074816-d933c7d2b988?auto=format&fit=crop&w=500&q=80",
            "stock": 120, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "RGB Gaming Mouse",
            "description": "25,600 DPI optical sensor with 11 programmable buttons and per-key RGB.",
            "price": 4999.00, "category": "Electronics", "tags": ["gaming", "mouse", "rgb"],
            "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?auto=format&fit=crop&w=500&q=80",
            "stock": 180, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Wireless Charging Pad",
            "description": "15W fast wireless charger compatible with all Qi devices, sleek glass finish.",
            "price": 1999.00, "category": "Electronics", "tags": ["charger", "wireless", "accessories"],
            "image_url": "https://images.unsplash.com/photo-1586953208448-b95a79798f07?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.2, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Mini Projector 4K",
            "description": "Pocket-size 4K projector with 1000 lumens and built-in Android TV.",
            "price": 29999.00, "category": "Electronics", "tags": ["projector", "4k", "home theater"],
            "image_url": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?auto=format&fit=crop&w=500&q=80",
            "stock": 40, "rating": 4.5, "created_at": datetime.utcnow()
        },

        # ── Wearables (8) ─────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Cyberpunk Smartwatch",
            "description": "Advanced health tracking with holographic UI, blood-oxygen, and stress monitoring.",
            "price": 15999.00, "category": "Wearables", "tags": ["smartwatch", "health", "cyberpunk"],
            "image_url": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&w=500&q=80",
            "stock": 50, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Fitness Tracker Band",
            "description": "Slim fitness band with heart rate, SpO2, sleep tracking, and 14-day battery.",
            "price": 3499.00, "category": "Wearables", "tags": ["fitness", "health", "band"],
            "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?auto=format&fit=crop&w=500&q=80",
            "stock": 250, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Smart Ring Health Monitor",
            "description": "Discreet smart ring tracking heart rate, temperature, and sleep quality.",
            "price": 22000.00, "category": "Wearables", "tags": ["ring", "health", "smart"],
            "image_url": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "GPS Running Watch",
            "description": "Pro running watch with built-in GPS, VO2 max, and route mapping.",
            "price": 28000.00, "category": "Wearables", "tags": ["running", "gps", "sports"],
            "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80",
            "stock": 70, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Smart Glasses Speaker",
            "description": "Stylish glasses with open-ear speakers, UV protection, and voice assistant.",
            "price": 18000.00, "category": "Wearables", "tags": ["glasses", "audio", "smart"],
            "image_url": "https://images.unsplash.com/photo-1574258495973-f010dfbb5371?auto=format&fit=crop&w=500&q=80",
            "stock": 35, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "ECG Smart Band",
            "description": "Medical-grade ECG monitoring wristband with instant heart health reports.",
            "price": 9999.00, "category": "Wearables", "tags": ["ecg", "medical", "health"],
            "image_url": "https://images.unsplash.com/photo-1510017803434-a899398421b3?auto=format&fit=crop&w=500&q=80",
            "stock": 90, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Kids Safety Smartwatch",
            "description": "GPS-enabled kids smartwatch with SOS button, geofencing, and video calling.",
            "price": 5999.00, "category": "Wearables", "tags": ["kids", "gps", "safety"],
            "image_url": "https://images.unsplash.com/photo-1551816230-ef5deaed4a26?auto=format&fit=crop&w=500&q=80",
            "stock": 100, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "VR Headset Pro",
            "description": "Standalone VR headset with 4K per eye display and full hand tracking.",
            "price": 59999.00, "category": "Wearables", "tags": ["vr", "gaming", "immersive"],
            "image_url": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?auto=format&fit=crop&w=500&q=80",
            "stock": 20, "rating": 4.8, "created_at": datetime.utcnow()
        },

        # ── Fashion (15) ──────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Aero-Glide Hover Sneakers",
            "description": "Ultra-lightweight footwear with magnetic lift technology.",
            "price": 20000.00, "category": "Fashion", "tags": ["shoes", "sneakers", "hover"],
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "LED Fiber-Optic Jacket",
            "description": "Smart jacket that changes color based on your mood and music.",
            "price": 10000.00, "category": "Fashion", "tags": ["jacket", "led", "clothing"],
            "image_url": "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=500&q=80",
            "stock": 120, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Thermo-Regulating Beanie",
            "description": "Smart beanie that automatically adjusts to your body temperature.",
            "price": 2800.00, "category": "Fashion", "tags": ["hat", "winter", "smart"],
            "image_url": "https://images.unsplash.com/photo-1576871337622-98d48d1cf531?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.1, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Classic Leather Backpack",
            "description": "Premium full-grain leather backpack with laptop compartment and USB port.",
            "price": 8500.00, "category": "Fashion", "tags": ["bag", "backpack", "leather"],
            "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=500&q=80",
            "stock": 150, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Slim Fit Chino Trousers",
            "description": "Stretch-cotton chino trousers in a modern slim fit, available in 8 colors.",
            "price": 2299.00, "category": "Fashion", "tags": ["trousers", "casual", "men"],
            "image_url": "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=500&q=80",
            "stock": 400, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Oversized Graphic Tee",
            "description": "100% organic cotton oversized tee with exclusive futuristic artwork.",
            "price": 1499.00, "category": "Fashion", "tags": ["tshirt", "graphic", "casual"],
            "image_url": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=500&q=80",
            "stock": 500, "rating": 4.2, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Chelsea Ankle Boots",
            "description": "Genuine suede Chelsea boots with elastic side panels and leather sole.",
            "price": 6999.00, "category": "Fashion", "tags": ["boots", "shoes", "suede"],
            "image_url": "https://images.unsplash.com/photo-1638247025967-b4e38f787b76?auto=format&fit=crop&w=500&q=80",
            "stock": 80, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Floral Summer Dress",
            "description": "Lightweight floral wrap dress perfect for summer outings and beach days.",
            "price": 2999.00, "category": "Fashion", "tags": ["dress", "summer", "women"],
            "image_url": "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Aviator Sunglasses",
            "description": "Classic gold-frame aviator sunglasses with UV400 polarized lenses.",
            "price": 3499.00, "category": "Fashion", "tags": ["sunglasses", "accessories", "uv"],
            "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=500&q=80",
            "stock": 250, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Luxury Silk Scarf",
            "description": "Hand-painted 100% pure silk scarf with traditional Indian motifs.",
            "price": 4200.00, "category": "Fashion", "tags": ["scarf", "silk", "women"],
            "image_url": "https://images.unsplash.com/photo-1601924994987-69e26d50dc26?auto=format&fit=crop&w=500&q=80",
            "stock": 100, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Slim Leather Wallet",
            "description": "Ultra-slim RFID-blocking genuine leather wallet with 8 card slots.",
            "price": 1800.00, "category": "Fashion", "tags": ["wallet", "leather", "accessories"],
            "image_url": "https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=500&q=80",
            "stock": 350, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Hooded Puffer Jacket",
            "description": "Lightweight down-fill puffer jacket with detachable hood, windproof.",
            "price": 5999.00, "category": "Fashion", "tags": ["jacket", "winter", "puffer"],
            "image_url": "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?auto=format&fit=crop&w=500&q=80",
            "stock": 120, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Ethnic Kurta Set",
            "description": "Hand-block printed pure cotton kurta with matching pyjama and dupatta.",
            "price": 3200.00, "category": "Fashion", "tags": ["ethnic", "kurta", "indian"],
            "image_url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=500&q=80",
            "stock": 180, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Canvas Tote Bag",
            "description": "Eco-friendly heavy-duty canvas tote bag with interior zipper pocket.",
            "price": 999.00, "category": "Fashion", "tags": ["bag", "tote", "eco"],
            "image_url": "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=500&q=80",
            "stock": 500, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Stainless Steel Watch",
            "description": "Minimalist stainless steel automatic watch with sapphire crystal glass.",
            "price": 12500.00, "category": "Fashion", "tags": ["watch", "minimalist", "steel"],
            "image_url": "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.8, "created_at": datetime.utcnow()
        },

        # ── Home & Living (12) ────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Levitating Planter",
            "description": "Magnetic levitating oak planter, perfect for bonsai or succulents.",
            "price": 7120.00, "category": "Home", "tags": ["decor", "plants", "levitating"],
            "image_url": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?auto=format&fit=crop&w=500&q=80",
            "stock": 80, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Smart Infinity Mirror",
            "description": "Displays time, weather, and your schedule within an endless optical illusion.",
            "price": 16800.00, "category": "Home", "tags": ["mirror", "smart home", "decor"],
            "image_url": "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=500&q=80",
            "stock": 25, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Nano-Leaf Light Panels",
            "description": "Modular RGB lighting panels that react to touch and sync with your setup.",
            "price": 15999.00, "category": "Home", "tags": ["lights", "rgb", "decor"],
            "image_url": "https://images.unsplash.com/photo-1565814329452-e1efa11c5b89?auto=format&fit=crop&w=500&q=80",
            "stock": 150, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Bamboo Bedding Set",
            "description": "Luxuriously soft 400-thread-count bamboo bed sheets with pillowcases.",
            "price": 4999.00, "category": "Home", "tags": ["bedding", "bamboo", "sleep"],
            "image_url": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Ergonomic Office Chair",
            "description": "Fully adjustable mesh office chair with lumbar support and headrest.",
            "price": 22000.00, "category": "Home", "tags": ["chair", "office", "ergonomic"],
            "image_url": "https://images.unsplash.com/photo-1580480055273-228ff5388ef8?auto=format&fit=crop&w=500&q=80",
            "stock": 40, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Scented Soy Candle Set",
            "description": "Set of 6 hand-poured soy wax candles in calming lavender and vanilla scents.",
            "price": 1899.00, "category": "Home", "tags": ["candle", "decor", "aromatherapy"],
            "image_url": "https://images.unsplash.com/photo-1602178506339-4eb39c89af35?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Minimalist Wall Clock",
            "description": "Silent sweep mechanism wall clock with walnut wood frame, 35cm diameter.",
            "price": 2500.00, "category": "Home", "tags": ["clock", "decor", "minimalist"],
            "image_url": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?auto=format&fit=crop&w=500&q=80",
            "stock": 120, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Indoor Herb Garden Kit",
            "description": "Self-watering indoor garden kit with LED grow lights, seeds included.",
            "price": 3999.00, "category": "Home", "tags": ["garden", "plants", "indoor"],
            "image_url": "https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?auto=format&fit=crop&w=500&q=80",
            "stock": 90, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Boho Macrame Wall Hanging",
            "description": "Handcrafted large macrame wall art, 90cm wide with natural cotton cord.",
            "price": 2200.00, "category": "Home", "tags": ["wall art", "boho", "handmade"],
            "image_url": "https://images.unsplash.com/photo-1522444195799-478538b28823?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Smart Air Purifier",
            "description": "HEPA + activated carbon air purifier with real-time air quality display.",
            "price": 12999.00, "category": "Home", "tags": ["air purifier", "health", "smart"],
            "image_url": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?auto=format&fit=crop&w=500&q=80",
            "stock": 55, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Floating Wooden Shelf",
            "description": "Set of 3 solid walnut floating wall shelves with hidden mounting brackets.",
            "price": 3400.00, "category": "Home", "tags": ["shelf", "storage", "wooden"],
            "image_url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=500&q=80",
            "stock": 100, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Electric Diffuser & Humidifier",
            "description": "Ultrasonic aroma diffuser with 7-color LED and auto-off safety feature.",
            "price": 1799.00, "category": "Home", "tags": ["diffuser", "aromatherapy", "humidifier"],
            "image_url": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.5, "created_at": datetime.utcnow()
        },

        # ── Gaming (10) ───────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Next-Gen Gaming Console",
            "description": "8K gaming console with ray-tracing, 2TB SSD, and 120fps support.",
            "price": 49999.00, "category": "Gaming", "tags": ["console", "gaming", "8k"],
            "image_url": "https://images.unsplash.com/photo-1607853202273-797f1c22a38e?auto=format&fit=crop&w=500&q=80",
            "stock": 30, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Pro Gaming Controller",
            "description": "Haptic feedback controller with adaptive triggers and 40hr battery life.",
            "price": 6999.00, "category": "Gaming", "tags": ["controller", "gaming", "haptic"],
            "image_url": "https://images.unsplash.com/photo-1592840496694-26d035b52b48?auto=format&fit=crop&w=500&q=80",
            "stock": 150, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Racing Gaming Chair",
            "description": "Ergonomic racing-style gaming chair with lumbar pillow and 180° recline.",
            "price": 18000.00, "category": "Gaming", "tags": ["chair", "gaming", "racing"],
            "image_url": "https://images.unsplash.com/photo-1598550476439-6847785fcea6?auto=format&fit=crop&w=500&q=80",
            "stock": 25, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Gaming Desk with LED",
            "description": "L-shaped gaming desk with built-in LED strip, cable management, and cup holder.",
            "price": 14999.00, "category": "Gaming", "tags": ["desk", "gaming", "led"],
            "image_url": "https://images.unsplash.com/photo-1593640495253-23196b27a87f?auto=format&fit=crop&w=500&q=80",
            "stock": 20, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Handheld Gaming Console",
            "description": "Portable gaming handheld with AMOLED display, 6hr battery, and 256GB storage.",
            "price": 24999.00, "category": "Gaming", "tags": ["handheld", "portable", "gaming"],
            "image_url": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Gaming Capture Card",
            "description": "4K60 HDR capture card for streaming and recording console gameplay.",
            "price": 9999.00, "category": "Gaming", "tags": ["capture card", "streaming", "gaming"],
            "image_url": "https://images.unsplash.com/photo-1614294149010-950b698f72c0?auto=format&fit=crop&w=500&q=80",
            "stock": 45, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Retro Mini Arcade Cabinet",
            "description": "Mini arcade cabinet with 10,000 classic games and 2-player joysticks.",
            "price": 8999.00, "category": "Gaming", "tags": ["arcade", "retro", "gaming"],
            "image_url": "https://images.unsplash.com/photo-1551103782-8ab07afd45c1?auto=format&fit=crop&w=500&q=80",
            "stock": 35, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Gaming Headset 7.1",
            "description": "Over-ear 7.1 surround gaming headset with noise-cancelling mic.",
            "price": 5499.00, "category": "Gaming", "tags": ["headset", "audio", "gaming"],
            "image_url": "https://images.unsplash.com/photo-1599669454699-248893623440?auto=format&fit=crop&w=500&q=80",
            "stock": 120, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Gaming Mousepad XL",
            "description": "Extended 900x400mm gaming mousepad with stitched edges and anti-slip base.",
            "price": 1299.00, "category": "Gaming", "tags": ["mousepad", "desk", "gaming"],
            "image_url": "https://images.unsplash.com/photo-1625842268584-8f3296236761?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Steering Wheel Racing Set",
            "description": "Force-feedback racing wheel with pedals and gear shifter for sim racing.",
            "price": 19999.00, "category": "Gaming", "tags": ["racing", "steering wheel", "simulation"],
            "image_url": "https://images.unsplash.com/photo-1547394765-185e1e68f34e?auto=format&fit=crop&w=500&q=80",
            "stock": 15, "rating": 4.7, "created_at": datetime.utcnow()
        },

        # ── Beauty (8) ────────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "AI Skin Analyzer",
            "description": "Scans your skin microscopically and formulates the perfect serum blend.",
            "price": 10320.00, "category": "Beauty", "tags": ["skincare", "health", "ai"],
            "image_url": "https://images.unsplash.com/photo-1596462502278-27bf85033e5a?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Sonic Facial Massager",
            "description": "Ultrasonic vibrations deeply clean pores and lift facial muscles.",
            "price": 3600.00, "category": "Beauty", "tags": ["skincare", "tool", "massage"],
            "image_url": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Vitamin C Brightening Serum",
            "description": "20% Vitamin C serum with hyaluronic acid for glowing, even-toned skin.",
            "price": 1999.00, "category": "Beauty", "tags": ["serum", "vitamin c", "skincare"],
            "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=500&q=80",
            "stock": 400, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Jade Gua Sha Tool",
            "description": "Authentic jade stone gua sha facial sculpting tool with carrying pouch.",
            "price": 899.00, "category": "Beauty", "tags": ["gua sha", "jade", "facial"],
            "image_url": "https://images.unsplash.com/photo-1612817288484-6f916006741a?auto=format&fit=crop&w=500&q=80",
            "stock": 250, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Professional Hair Dryer",
            "description": "1800W ionic hair dryer with ceramic technology for frizz-free blowouts.",
            "price": 4500.00, "category": "Beauty", "tags": ["hair", "dryer", "ionic"],
            "image_url": "https://images.unsplash.com/photo-1522338242992-e1a54906a8da?auto=format&fit=crop&w=500&q=80",
            "stock": 130, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Retinol Night Cream",
            "description": "Advanced retinol + peptide night cream for anti-aging and skin renewal.",
            "price": 2799.00, "category": "Beauty", "tags": ["night cream", "retinol", "anti-aging"],
            "image_url": "https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?auto=format&fit=crop&w=500&q=80",
            "stock": 180, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "LED Face Mask Therapy",
            "description": "7-color LED photon therapy mask for acne, wrinkles, and skin rejuvenation.",
            "price": 7999.00, "category": "Beauty", "tags": ["led", "mask", "therapy"],
            "image_url": "https://images.unsplash.com/photo-1616394584738-fc6e612e71b9?auto=format&fit=crop&w=500&q=80",
            "stock": 50, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Matte Lipstick Set",
            "description": "Long-lasting 12-shade matte lipstick collection, cruelty-free formula.",
            "price": 1299.00, "category": "Beauty", "tags": ["lipstick", "makeup", "matte"],
            "image_url": "https://images.unsplash.com/photo-1586495777744-4e6232bf8d13?auto=format&fit=crop&w=500&q=80",
            "stock": 500, "rating": 4.6, "created_at": datetime.utcnow()
        },

        # ── Wellness (8) ──────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Quantum Sleep Pod",
            "description": "Sensory deprivation tent for your bed inducing deep REM sleep via binaural beats.",
            "price": 68000.00, "category": "Wellness", "tags": ["sleep", "health", "bed"],
            "image_url": "https://images.unsplash.com/photo-1505691938895-1758d7feb511?auto=format&fit=crop&w=500&q=80",
            "stock": 10, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Yoga Mat Premium",
            "description": "6mm thick non-slip natural rubber yoga mat with alignment lines.",
            "price": 2499.00, "category": "Wellness", "tags": ["yoga", "fitness", "mat"],
            "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Meditation Cushion Set",
            "description": "Buckwheat-filled zafu and zabuton meditation cushion set in organic cotton.",
            "price": 3200.00, "category": "Wellness", "tags": ["meditation", "yoga", "cushion"],
            "image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=500&q=80",
            "stock": 100, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Resistance Band Set",
            "description": "Set of 5 fabric resistance bands with varying tension levels for home workouts.",
            "price": 999.00, "category": "Wellness", "tags": ["fitness", "resistance", "workout"],
            "image_url": "https://images.unsplash.com/photo-1598289431512-b97b0917affc?auto=format&fit=crop&w=500&q=80",
            "stock": 500, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Foam Roller Massager",
            "description": "High-density EVA foam roller for muscle recovery, trigger point release.",
            "price": 1299.00, "category": "Wellness", "tags": ["massage", "recovery", "fitness"],
            "image_url": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.3, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Electric Massage Gun",
            "description": "Deep tissue percussion massage gun with 6 heads and 20 speed settings.",
            "price": 4999.00, "category": "Wellness", "tags": ["massage", "recovery", "electric"],
            "image_url": "https://images.unsplash.com/photo-1608138278651-60b9c0f0e4fa?auto=format&fit=crop&w=500&q=80",
            "stock": 80, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Whey Protein Chocolate",
            "description": "25g protein per serving, chocolate fudge flavour, 2kg tub, lab-tested.",
            "price": 3499.00, "category": "Wellness", "tags": ["protein", "supplement", "gym"],
            "image_url": "https://images.unsplash.com/photo-1593095948071-474c5cc2989d?auto=format&fit=crop&w=500&q=80",
            "stock": 150, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Acupressure Mat & Pillow",
            "description": "Bed of nails acupressure mat with pillow for back pain and stress relief.",
            "price": 1799.00, "category": "Wellness", "tags": ["acupressure", "pain relief", "yoga"],
            "image_url": "https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=500&q=80",
            "stock": 160, "rating": 4.4, "created_at": datetime.utcnow()
        },

        # ── Sports (8) ────────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Cricket Bat English Willow",
            "description": "Grade 1 English willow cricket bat, full size, with grip and cover.",
            "price": 8999.00, "category": "Sports", "tags": ["cricket", "bat", "outdoor"],
            "image_url": "https://images.unsplash.com/photo-1531415074968-036ba1b575da?auto=format&fit=crop&w=500&q=80",
            "stock": 50, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Football Nike Strike",
            "description": "FIFA approved match football with high-visibility graphic and durable casing.",
            "price": 2499.00, "category": "Sports", "tags": ["football", "soccer", "outdoor"],
            "image_url": "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=500&q=80",
            "stock": 200, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Adjustable Dumbbells 20kg",
            "description": "Space-saving adjustable dumbbells from 2.5kg to 20kg per hand.",
            "price": 12999.00, "category": "Sports", "tags": ["dumbbells", "gym", "weights"],
            "image_url": "https://images.unsplash.com/photo-1517963879433-6ad2b056d712?auto=format&fit=crop&w=500&q=80",
            "stock": 40, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Badminton Racket Pro",
            "description": "Lightweight carbon fiber badminton racket with extra string set.",
            "price": 3299.00, "category": "Sports", "tags": ["badminton", "racket", "indoor"],
            "image_url": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=500&q=80",
            "stock": 80, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Swimming Goggles Anti-Fog",
            "description": "UV-protected anti-fog swimming goggles with wide vision and soft silicone seal.",
            "price": 899.00, "category": "Sports", "tags": ["swimming", "goggles", "water"],
            "image_url": "https://images.unsplash.com/photo-1530549387789-4c1017266635?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Treadmill Foldable Home",
            "description": "Foldable motorized treadmill with 12 preset programs and LCD display.",
            "price": 35000.00, "category": "Sports", "tags": ["treadmill", "cardio", "gym"],
            "image_url": "https://images.unsplash.com/photo-1538805060514-97d9cc17730c?auto=format&fit=crop&w=500&q=80",
            "stock": 15, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Cycling Helmet MIPS",
            "description": "Aerodynamic MIPS cycling helmet with 22 ventilation channels, 280g.",
            "price": 5499.00, "category": "Sports", "tags": ["cycling", "helmet", "safety"],
            "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Skateboard Complete",
            "description": "7-ply maple complete skateboard with ABEC-9 bearings and grip tape.",
            "price": 3999.00, "category": "Sports", "tags": ["skateboard", "outdoor", "street"],
            "image_url": "https://images.unsplash.com/photo-1547447134-cd3f5c716030?auto=format&fit=crop&w=500&q=80",
            "stock": 70, "rating": 4.4, "created_at": datetime.utcnow()
        },

        # ── Kitchen (8) ───────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Smart Air Fryer 6L",
            "description": "Digital air fryer with 12 cooking presets, touch display, and 6L capacity.",
            "price": 7999.00, "category": "Kitchen", "tags": ["air fryer", "cooking", "smart"],
            "image_url": "https://images.unsplash.com/photo-1648146288804-14fe9fbbad34?auto=format&fit=crop&w=500&q=80",
            "stock": 100, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Pour-Over Coffee Set",
            "description": "Handblown borosilicate glass pour-over coffee maker with gooseneck kettle.",
            "price": 3200.00, "category": "Kitchen", "tags": ["coffee", "pour over", "brewing"],
            "image_url": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=500&q=80",
            "stock": 150, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Cast Iron Skillet 10-inch",
            "description": "Pre-seasoned cast iron skillet for stovetop, oven, and campfire cooking.",
            "price": 2499.00, "category": "Kitchen", "tags": ["skillet", "cast iron", "cooking"],
            "image_url": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?auto=format&fit=crop&w=500&q=80",
            "stock": 120, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "High-Speed Blender",
            "description": "2000W professional blender with self-cleaning function and 2L jar.",
            "price": 8999.00, "category": "Kitchen", "tags": ["blender", "smoothie", "cooking"],
            "image_url": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?auto=format&fit=crop&w=500&q=80",
            "stock": 60, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Bamboo Cutting Board Set",
            "description": "Set of 3 organic bamboo cutting boards with juice grooves and handles.",
            "price": 1599.00, "category": "Kitchen", "tags": ["cutting board", "bamboo", "eco"],
            "image_url": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=500&q=80",
            "stock": 250, "rating": 4.4, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Espresso Machine",
            "description": "15-bar pump espresso machine with built-in steam wand and milk frother.",
            "price": 14999.00, "category": "Kitchen", "tags": ["espresso", "coffee", "machine"],
            "image_url": "https://images.unsplash.com/photo-1510017803434-a899398421b3?auto=format&fit=crop&w=500&q=80",
            "stock": 35, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Non-Stick Cookware Set",
            "description": "10-piece non-stick cookware set with granite coating and glass lids.",
            "price": 5999.00, "category": "Kitchen", "tags": ["cookware", "non-stick", "set"],
            "image_url": "https://images.unsplash.com/photo-1584990347449-a5d9f800a783?auto=format&fit=crop&w=500&q=80",
            "stock": 80, "rating": 4.5, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Instant Pot 7-in-1",
            "description": "Multi-use pressure cooker, slow cooker, rice cooker, steamer, and more.",
            "price": 9499.00, "category": "Kitchen", "tags": ["instant pot", "pressure cooker", "multi cooker"],
            "image_url": "https://images.unsplash.com/photo-1556909172-54557c7e4fb7?auto=format&fit=crop&w=500&q=80",
            "stock": 90, "rating": 4.7, "created_at": datetime.utcnow()
        },

        # ── Books (8) ─────────────────────────────────────────────────────
        {
            "_id": str(uuid.uuid4()), "title": "Atomic Habits",
            "description": "James Clear's #1 bestseller on building good habits and breaking bad ones.",
            "price": 499.00, "category": "Books", "tags": ["self-help", "habits", "bestseller"],
            "image_url": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=500&q=80",
            "stock": 500, "rating": 4.9, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "The Psychology of Money",
            "description": "Morgan Housel's timeless lessons on wealth, greed, and happiness.",
            "price": 399.00, "category": "Books", "tags": ["finance", "money", "bestseller"],
            "image_url": "https://images.unsplash.com/photo-1554672408-17407c4e1f76?auto=format&fit=crop&w=500&q=80",
            "stock": 400, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Sapiens: A Brief History",
            "description": "Yuval Noah Harari's groundbreaking narrative of humankind's history.",
            "price": 599.00, "category": "Books", "tags": ["history", "non-fiction", "bestseller"],
            "image_url": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=500&q=80",
            "stock": 350, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Zero to One",
            "description": "Peter Thiel's notes on startups and how to build the future.",
            "price": 449.00, "category": "Books", "tags": ["startup", "business", "entrepreneurship"],
            "image_url": "https://images.unsplash.com/photo-1589998059171-988d887df646?auto=format&fit=crop&w=500&q=80",
            "stock": 300, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Deep Work",
            "description": "Cal Newport's rules for focused success in a distracted world.",
            "price": 399.00, "category": "Books", "tags": ["productivity", "focus", "self-help"],
            "image_url": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=500&q=80",
            "stock": 400, "rating": 4.7, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "The Alchemist",
            "description": "Paulo Coelho's magical novel about following your dreams and destiny.",
            "price": 299.00, "category": "Books", "tags": ["fiction", "novel", "classic"],
            "image_url": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=500&q=80",
            "stock": 600, "rating": 4.8, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Rich Dad Poor Dad",
            "description": "Robert Kiyosaki's classic on financial literacy and building wealth.",
            "price": 349.00, "category": "Books", "tags": ["finance", "investing", "bestseller"],
            "image_url": "https://images.unsplash.com/photo-1490633874781-1c63cc424610?auto=format&fit=crop&w=500&q=80",
            "stock": 450, "rating": 4.6, "created_at": datetime.utcnow()
        },
        {
            "_id": str(uuid.uuid4()), "title": "Think and Grow Rich",
            "description": "Napoleon Hill's classic motivational book on success and wealth mindset.",
            "price": 299.00, "category": "Books", "tags": ["motivation", "wealth", "classic"],
            "image_url": "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=500&q=80",
            "stock": 400, "rating": 4.6, "created_at": datetime.utcnow()
        },
    ]

    await db["products"].insert_many(products)
    print(f"Database seeded with {len(products)} products across {len(set(p['category'] for p in products))} categories!")
    client.close()

if __name__ == "__main__":
    asyncio.run(seed_data())
