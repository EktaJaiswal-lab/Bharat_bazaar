# Bharat Bazaar

An AI-powered e-commerce platform with personalized product recommendations, smart search, and an intelligent shopping assistant. Built with React, FastAPI, MongoDB, and Google Gemini.

**Repository:** [https://github.com/EktaJaiswal-lab/Bharat_bazaar](https://github.com/EktaJaiswal-lab/Bharat_bazaar)

---

## Features

- **Product catalog** — Browse 100+ products across 10 categories (Electronics, Fashion, Beauty, Home & Living, and more)
- **Hybrid recommendations** — Content-based + collaborative filtering using scikit-learn
- **Smart search** — TF-IDF search with MongoDB fallback on title, category, and tags
- **AI chatbot** — Gemini-powered assistant with local FAQ fallback when offline
- **User authentication** — JWT-based signup and login
- **Shopping cart** — Add items and manage cart from the UI
- **Analytics dashboard** — Sales and category insights with charts
- **Admin tools** — Add new products from the frontend

---

## Tech Stack

| Layer      | Technologies |
|-----------|--------------|
| Frontend  | React 19, Vite, Tailwind CSS, React Router, Axios, Recharts |
| Backend   | FastAPI, Uvicorn, Motor (MongoDB), Pydantic, JWT |
| Database  | MongoDB |
| AI / ML   | Google Gemini (`google-genai`), scikit-learn, pandas, numpy |

---

## Project Structure

```
Bharat_bazaar/
├── backend/
│   ├── ai/              # Chatbot engine
│   ├── ml/              # Recommendation engine
│   ├── models/          # Pydantic models
│   ├── routes/          # API routes (auth, products, chat, etc.)
│   ├── main.py          # FastAPI entry point
│   ├── seed.py          # Database seeding script
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/  # Navbar, Footer, Chatbot, Cart
    │   ├── context/     # Auth & Cart state
    │   └── pages/       # Home, Products, Dashboard, etc.
    └── package.json
```

---

## Prerequisites

- **Python** 3.10+
- **Node.js** 18+
- **MongoDB** running locally (default: `mongodb://localhost:27017`)
- **Google Gemini API key** (optional — chatbot falls back to local FAQs without it)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/EktaJaiswal-lab/Bharat_bazaar.git
cd Bharat_bazaar
```

### 2. Backend setup

```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file in `backend/`:

```env
MONGODB_URL=mongodb://localhost:27017
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
```

Seed the database:

```bash
python seed.py
```

Start the API server:

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API docs: **http://localhost:8000/docs**

### 3. Frontend setup

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

App URL: **http://localhost:5173**

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/auth/signup` | Register a new user |
| POST | `/auth/login` | Login and get JWT token |
| GET | `/products/` | List products (optional `category`, `skip`, `limit`) |
| GET | `/products/search/?q=` | Search products |
| GET | `/products/{id}` | Get product by ID |
| GET | `/products/{id}/similar` | Similar products |
| GET | `/products/recommendations/personalized` | Personalized recommendations |
| POST | `/products/` | Create a product |
| POST | `/interactions/` | Log user interactions |
| POST | `/chat/` | Chat with AI assistant |
| GET | `/analytics/dashboard` | Dashboard analytics |

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MONGODB_URL` | MongoDB connection string | Yes |
| `SECRET_KEY` | JWT signing secret | Yes |
| `GEMINI_API_KEY` | Google Gemini API key for chatbot | Optional |

---

## Pages

| Route | Description |
|-------|-------------|
| `/` | Home with personalized recommendations |
| `/products` | Product listing and search |
| `/products/:id` | Product details and similar items |
| `/categories` | Browse by category |
| `/login` | User login |
| `/register` | User registration |
| `/dashboard` | Analytics dashboard |
| `/add-product` | Add new product |
| `/returns` | Return policy page |

---

## Notes

- First backend startup may take 1–2 minutes while ML libraries load and the recommendation engine trains.
- Without a Gemini API key, the chatbot uses built-in FAQ responses for common questions (shipping, returns, payments, etc.).
- Do not commit `.env` files — they are listed in `.gitignore`.

---

## License

This project is for educational and portfolio use.
