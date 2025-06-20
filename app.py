import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyA4E3l7WIBq0X1mxBS8_QhUzGaxmuJi-6g")
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="CookPal - AI Cooking Assistant", layout="centered")

st.markdown("## 🍳 CookPal – Your Friendly AI Cooking Companion")
st.markdown("Ask me anything about cooking, recipes, ingredients, or meal plans!")

user_input = st.chat_input("What do want to cook? Describe it...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(user_input)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
