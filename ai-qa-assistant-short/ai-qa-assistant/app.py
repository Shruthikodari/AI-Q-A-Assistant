import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API Key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ OpenAI API key not found! Please set OPENAI_API_KEY in your .env file or system environment.")
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Internship guidelines (add only important Q&A answers here)
guidelines = {
    "project submission": "Project submissions must be submitted on **https://code.swecha.org**. You cannot use GitHub for submission.",
    "attendance": "Attendance is mandatory in the morning sessions (9:30 AM – 10:00 AM).",
    "communication": "Official communication is through the **Communication Board**, not WhatsApp."
}

# Function to get answer
def get_answer(query: str):
    query_lower = query.lower()

    # 1. Check guidelines first
    for key, value in guidelines.items():
        if key in query_lower:
            return value, "📚 Internship Guidelines"

    # 2. Else, ask OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for internship training sessions."},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content, "🌐 OpenAI"
    except Exception as e:
        return f"⚠️ Error: {str(e)}", "❌ System"

# ------------------- Streamlit UI -------------------
st.set_page_config(page_title="Internship Q&A Assistant", page_icon="🤝", layout="centered")

st.markdown("## 🚀 Welcome to Internship Training Q&A Assistant 🤝")
st.markdown("Your friendly AI guide for internship training sessions 📚")

query = st.text_input("💬 Ask your question:", placeholder="Type here...")

if query:
    answer, source = get_answer(query)

    # ✅ Use st.success to display clearly
    st.success(f"✨ Here's your answer:\n\n{answer}\n\n🔎 Source: {source}")


