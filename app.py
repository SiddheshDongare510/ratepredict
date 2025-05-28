import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import numpy as np

# -------------------- UI Configuration --------------------
st.set_page_config(page_title="Real Estate Rate Predictor", layout="centered")
st.markdown("<h1 style='color:#124f7c;'>🏠 Real Estate Rate Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#fa6801;'>Enter property details to get an estimated price and confidence score.</p>", unsafe_allow_html=True)

# -------------------- Input Fields --------------------
lat = st.number_input("📍 Latitude", value=18.5204, format="%.6f")
lon = st.number_input("📍 Longitude", value=73.8567, format="%.6f")

categories = {
    "Apartment": ["Flat"],
    "Banquet Hall": ["Marriage Garden"],
    "Bungalow / Villa": ["Individual Bungalow", "Row House", "Villa"],
    "Commercial Plot": ["Commercial Plot", "Commercial Premise"],
    "Factory": ["Industrial", "Industrial Plot"],
    "Gala": ["Industrial Gala", "Market Yard"],
    "Hostel": ["PG properties"],
    "Hotel": ["Hotel and Restaurant properties", "Restaurant"],
    "Plot": ["Plot LAP", "Plot - LAP", "Vacant Plot", "Plot + Construction"],
    "Multi-Dwelling Units>=3": [""],
    "Office": [""],
    "Resort": [""],
    "School": [""],
    "Shop": [""],
    "Farmhouse": [""],
    "Warehouse": [""],
    "Godown": [""],
    "Hospital": [""]
}

category = st.selectbox("🏷️ Category", list(categories.keys()))
subcategory = st.selectbox("📂 Subcategory", categories[category])

# -------------------- Dummy ML Prediction Logic --------------------
def predict_rate(lat, lon, category, subcategory):
    """
    A simulated prediction function that gives an estimated rate based on lat, lon.
    (Replace with real ML model in future.)
    """
    np.random.seed(int((lat + lon) * 10000) % 1000)
    base_rate = np.random.uniform(3000, 15000)  # INR per sq.ft
    confidence = np.random.uniform(0.6, 0.95)   # Confidence Score
    return round(base_rate, 2), round(confidence, 2)

# -------------------- Prediction & Output --------------------
if st.button("🎯 Predict Rate"):
    rate, confidence = predict_rate(lat, lon, category, subcategory)
    st.success(f"💰 Estimated Rate: ₹{rate} per sq.ft")
    st.info(f"📊 Confidence Score: {confidence * 100:.2f}%")

    # Map view
    m = folium.Map(location=[lat, lon], zoom_start=14)
    folium.Marker([lat, lon], popup=f"{category} - {subcategory}", icon=folium.Icon(color="orange")).add_to(m)
    st.markdown("### 🗺️ Location Map")
    folium_static(m)

