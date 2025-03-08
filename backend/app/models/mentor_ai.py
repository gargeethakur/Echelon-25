import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ask_mentor(question: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text
