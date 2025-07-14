import streamlit as st
import requests
from gemini_extractor import generate_clinical_output

st.title("🧠 Clinical Entity Extractor")

# Input: user_id and template_id side-by-side
col1, col2 = st.columns(2)
with col1:
    user_id = st.number_input("👤 User ID", min_value=1)
with col2:
    template_id = st.number_input("📄 Template ID", min_value=1)

# Fetch Sections button centered
if st.button("📥 Fetch Sections"):
    try:
        params = {"user_id": user_id, "template_id": template_id}
        res = requests.get("http://localhost:8000/get_sections_combined/", params=params)

        if res.status_code == 200:
            data = res.json()
            if "sections_combined" in data:
                st.session_state["sections_content"] = data["sections_combined"]
                st.success("✅ Sections fetched successfully.")
            else:
                st.warning(data.get("error", "Unknown issue occurred"))
        else:
            st.error("❌ Failed to fetch sections.")

    except Exception as e:
        st.error(f"⚠️ Exception: {e}")

# Text area: Sections content
sections_content = st.text_area("📑 Sections Content", value=st.session_state.get("sections_content", ""), height=200)

# Text area: Transcript input
transcript = st.text_area("🩺 Transcript", height=200)

# Submit button
if st.button("🚀 Submit to Gemini"):
    if not sections_content or not transcript:
        st.warning("⚠️ Please provide sections content and transcript.")
    else:
        combined_text = sections_content.strip() + "\n\n" + transcript.strip()
        with st.spinner("Sending to Gemini..."):
            response = generate_clinical_output(combined_text)
            st.text_area("🤖 AI Answer", value=response, height=400)
