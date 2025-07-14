import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_clinical_output(combined_text: str):
    clinical_prompt = f"""

{combined_text}

"""
    try:
        response = model.generate_content(clinical_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
