import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class ChatbotEngine:
    def __init__(self):
        if GEMINI_API_KEY:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-flash') # Using the fast, cost-effective model
            self.is_configured = True
        else:
            self.is_configured = False
            print("WARNING: GEMINI_API_KEY not found in environment. Chatbot will be disabled.")
            
        self.system_prompt = """
You are the Bharat Bazaar AI Assistant, a helpful, futuristic, and premium customer support agent for an AI-powered e-commerce platform called 'Bharat Bazaar'.
Your goals are to:
1. Help customers find products.
2. Answer questions about the store's return policy (30-day hassle-free returns on all items).
3. Provide recommendations based on their queries.
4. Maintain a polite, concise, and slightly futuristic/tech-savvy tone.

Keep your responses short and formatting clean using Markdown if needed. Do not make up product prices or features unless giving a hypothetical example.
"""

    async def get_response(self, message: str, history: list = None):
        if not self.is_configured:
            return "I'm currently offline as my AI core (GEMINI_API_KEY) is not configured. Please contact the administrator."
            
        try:
            # Construct the conversation history
            contents = [{"role": "user", "parts": [self.system_prompt]}]
            contents.append({"role": "model", "parts": ["Understood. I am the Bharat Bazaar AI Assistant, ready to help."]})
            
            if history:
                for msg in history:
                    role = "user" if msg["role"] == "user" else "model"
                    contents.append({"role": role, "parts": [msg["content"]]})
                    
            # Add the current message
            contents.append({"role": "user", "parts": [message]})
            
            response = self.model.generate_content(contents)
            return response.text
            
        except Exception as e:
            print(f"Chatbot Error: {e}")
            return "I'm experiencing some technical difficulties in my neural net right now. Please try again later."

chatbot_engine = ChatbotEngine()
