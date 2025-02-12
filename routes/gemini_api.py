import google.generativeai as genai
import os


GENAI_API_KEY = "AIzaSyAHPrEYNFO6JOdb1bvogqAvk1Xua3Rrf6E"

genai.configure(api_key=GENAI_API_KEY)

def get_ai_suggestions(user_query):
    model = genai.GenerativeModel('gemini-pro')

    try:
        response = model.generate_content(f"""
            Based on the query: '{user_query}', provide the most relevant club categories found in an academic or college environment.
            The categories should be directly usable for searching in a student club database.
            Return only a **comma-separated list** of categories (e.g., "Dance, Music, Cyber, Debate, Sports").
        """)

        print(f"🔍 AI Raw Response: {response.text}")  

        if response and response.text:
            categories = response.text.split(",")  
            return [cat.strip().lower() for cat in categories]
    except Exception as e:
        print("Error in AI Search:", e)
        return []

    return []

def ask_gemini(question):
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(f"Answer this academic or faculty-related question: {question}")
    
    if response and response.text:
        return response.text.strip()
    
    return "Sorry, I couldn't find an answer. Please try again!"