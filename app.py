import streamlit as st
import numpy as np
import requests

# --- Page Configuration ---
st.set_page_config(page_title="Property Rate Predictor", layout="centered")

st.markdown(
    "<h1 style='color:#124f7c;'>🏠 Smart Property Rate Estimator</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#fa6801;'>Enter your property location and category to get estimated market rates with area insights.</p>", 
    unsafe_allow_html=True
)

# --- Input Section ---
lat = st.number_input("Enter Latitude", format="%.6f", step=0.000001)
lon = st.number_input("Enter Longitude", format="%.6f", step=0.000001)

# Category list (flattened)
property_types = [
    "Apartment", "Flat", "Banquet Hall", "Marriage Garden", "Bungalow", "Villa", "Row House",
    "Commercial Plot", "Commercial Premise", "Factory", "Industrial", "Industrial Plot",
    "Gala", "Market Yard", "Hostel", "PG properties", "Hotel", "Restaurant", "Plot", 
    "Vacant Plot", "Plot + Construction", "Multi-Dwelling Units", "Office", "Resort", 
    "School", "Shop", "Farmhouse", "Warehouse", "Godown", "Hospital"
]
category = st.selectbox("Select Property Category", sorted(property_types))

# --- Predict Button ---
if st.button("🔍 Predict Rate"):

    # --- Dummy Prediction Logic (replace with actual model later) ---
    np.random.seed(int((lat + lon)*1000) % 999)
    predicted_rate = np.random.randint(3000, 12000)
    confidence = round(np.random.uniform(0.82, 0.97), 2)

    st.success(f"💰 Estimated Rate: ₹{predicted_rate} per sq.ft")
    st.info(f"Confidence Score: {confidence*100}%")

    # --- Map View ---
    st.map(data={"lat": [lat], "lon": [lon]})

    # --- Reverse Geocoding ---
    def get_area_name(lat, lon):
        try:
            url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=14&addressdetails=1"
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            data = response.json()
            area_name = data['address'].get('suburb') or data['address'].get('city_district') or data['address'].get('city') or "your location"
            return area_name
        except:
            return "your location"

    # --- AI-Generated Area Summary ---
    def generate_area_summary(area_name, category):
        summaries = [
            f"{area_name} is witnessing increasing traction for {category.lower()} properties. Infrastructure projects and better amenities have driven demand.",
            f"The real estate trend in {area_name} shows consistent growth in {category.lower()} pricing, especially in gated communities and premium builds.",
            f"{area_name} is rapidly becoming a hub for {category.lower()} investments with strong rental yield and resale value.",
            f"Due to growing connectivity and lifestyle upgrades, {category.lower()} sales are rising in {area_name}.",
            f"{area_name} has emerged as a preferred destination for modern {category.lower()} developments, particularly among professionals and young families."
        ]
        np.random.seed(len(area_name) + len(category))
        return np.random.choice(summaries)

    area_name = get_area_name(lat, lon)
    summary = generate_area_summary(area_name, category)

    st.markdown("### 🧠 AI-Powered Area Insight")
    st.markdown(f"<div style='color:#124f7c; font-size: 16px; background-color:#fff7f0; padding:10px; border-radius:10px'>{summary}</div>", unsafe_allow_html=True)
