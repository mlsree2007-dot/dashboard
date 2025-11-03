import streamlit as st
import requests

st.title("📚 Smart Book Locator Dashboard")

api_url = "https://smart-31fj.onrender.com"  # Use your actual Render URL

if st.button("Scan Book"):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        st.success(f"📘 Book ID: {data['tag_id']}")
        st.info(f"📍 Location: {data['location']}")
        st.caption(f"🕒 Scanned at: {data['timestamp']}")
    else:
        st.error("Failed to fetch scan data")
