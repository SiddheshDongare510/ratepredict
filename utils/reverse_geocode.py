# utils/reverse_geocode.py
import requests

def reverse_geocode(lat, lon):
    """
    Reverse geocode using OpenStreetMap Nominatim API.
    Returns a human-readable address.
    """
    url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('display_name', 'Unknown location')
        else:
            return "Error retrieving location"
    except Exception as e:
        return str(e)

# Example usage (you can remove this in prod)
if __name__ == '__main__':
    print(reverse_geocode(19.0760, 72.8777))  # Mumbai
