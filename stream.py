import streamlit as st
import requests

st.title("📚 Smart Book Locator Dashboard")

# Replace with your actual Render API URL
api_url = "https://smart-5.onrender.com"

# Search bar
book_id = st.text_input("🔍 Enter Book ID to locate")

if st.button("Search"):
    if book_id:
        response = requests.get(f"{api_url}?tag_id={book_id}")
        if response.status_code == 200:
            data = response.json()
            if data.get("found"):
                st.success(f"📘 Book ID: {data['tag_id']}")
                st.info(f"📍 Location: {data['location']}")
                st.caption(f"🕒 Last seen: {data['timestamp']}")
            else:
                st.warning("Book not found in system.")
        else:
            st.error("Failed to fetch data from API.")
    else:
        st.warning("Please enter a Book ID.")
