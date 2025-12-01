import requests
import json

CACHE_FILE = "cache/bugcrowd.json"

def load_cache():
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def fetch_bugcrowd():
    """Fetches public programs from Bugcrowd."""
    url = "https://bugcrowd.com/programs.json"
    items = []

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            json_data = response.json()

            for program in json_data.get("programs", []):
                items.append(program.get("name"))
    except Exception as e:
        print("Error fetching Bugcrowd:", e)

    return items
