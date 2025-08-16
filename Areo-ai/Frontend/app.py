import streamlit as st
import requests

st.set_page_config(page_title="MOSDAC AI Help Bot", page_icon="🛰️")

st.title("🛰️ MOSDAC AI Help Bot")
st.markdown("Ask any question related to satellite data, products, or missions.")

query = st.text_input("Your Question:")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask/",
                json={"question": query}
            )
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                st.success(f"Answer: {answer}")
            else:
                st.error("⚠️ Backend error. Check if Django server is running.")
        except Exception as e:
            st.error(f"❌ Request failed: {e}")
