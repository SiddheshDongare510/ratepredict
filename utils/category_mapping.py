# utils/category_mapping.py

CATEGORY_MAPPING = {
    "Apartment": ["Flat"],
    "Banquet Hall": ["Marriage Garden"],
    "Bungalow / Villa": ["Individual Bungalow", "Row House", "Villa"],
    "Commercial Plot": ["Commercial Plot", "Commercial Premise"],
    "Factory": ["Industrial", "Industrial Plot"],
    "Gala": ["Industrial Gala", "Market Yard"],
    "Hostel": ["PG properties"],
    "Hotel": ["Hotel and Restaurant properties", "Restaurant"],
    "Plot": ["Plot LAP", "Plot - LAP", "Vacant Plot", "Plot + Construction"],
    "Multi-Dwelling Units": [">=3"],
    "Office": [],
    "Resort": [],
    "School": [],
    "Shop": [],
    "Farmhouse": [],
    "Warehouse": [],
    "Godown": [],
    "Hospital": []
}

def normalize_category(subcategory: str):
    for main_cat, subcats in CATEGORY_MAPPING.items():
        if subcategory in subcats or subcategory == main_cat:
            return main_cat
    return "Other"
