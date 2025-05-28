import requests

# Reverse Geocoding using Nominatim (OpenStreetMap)
def get_area_name(lat, lon):
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=14&addressdetails=1"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = response.json()
        area_name = data['address'].get('suburb') or data['address'].get('city_district') or data['address'].get('city') or "Local Area"
        return area_name
    except:
        return "Unknown Area"

# AI-Style Summary Generator (Simulated)
def generate_area_summary(area_name, category):
    summaries = [
        f"{area_name} has seen a steady rise in demand for {category.lower()}s, especially over the last 12 months. Real estate developers are focusing on modern layouts and gated societies.",
        f"The {category.lower()} market in {area_name} is growing, with notable appreciation in property rates due to improved infrastructure and metro connectivity.",
        f"{area_name} remains a hotbed for {category.lower()} investments. Buyers are especially interested in resale properties with high rental yield potential.",
        f"{area_name} is attracting attention for new {category.lower()} projects backed by reputed builders. Affordability and connectivity are key drivers here.",
        f"In recent quarters, {area_name} has shown consistent growth in {category.lower()} pricing. Investor interest remains strong in under-construction projects."
    ]
    np.random.seed(len(area_name) + len(category))
    return np.random.choice(summaries)

# Add this after prediction and map rendering:
    area_name = get_area_name(lat, lon)
    ai_summary = generate_area_summary(area_name, category)
    st.markdown("### 🧠 AI-Generated Area Insight")
    st.markdown(f"**{ai_summary}**")
