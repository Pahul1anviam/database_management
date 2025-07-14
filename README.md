Clinical Documentation Streamlit App
=====================================

Overview:
---------
This project is a clinical documentation tool that allows users to:
- Fetch section data based on user ID and template ID
- Input a medical transcript
- Submit the combined content to the Gemini AI model
- Receive a structured clinical output

Technologies Used:
------------------
- Streamlit (Frontend)
- FastAPI (Backend)
- SQLite (Database)
- Google Gemini (LLM API)
- Python, SQLAlchemy, Requests, Dotenv

How to Run:
-----------
1. Install all required packages:
   pip install -r requirements.txt

2. Start the FastAPI backend:
   uvicorn app.main:app --reload

3. Run the Streamlit interface:
   streamlit run streamlit.py

Environment Setup:
------------------
Create a `.env` file in the root directory and add your Gemini API key:
GOOGLE_API_KEY=your-gemini-api-key

Usage Steps:
------------
1. Enter User ID and Template ID.
2. Click "Fetch Sections" to get related section content from the database.
3. Paste your medical transcript.
4. Click "Submit to Gemini" to get structured data as AI output.

Folder Structure:
-----------------
- app/
  - CRUD operations
  - Database models
  - API routes
- streamlit.py (frontend)
- gemini_extractor.py (LLM prompt logic)
- templates.db (SQLite database)
- .env (environment variables)
- README.txt

Note:
-----
This is a prototype application for clinical use-case testing.
