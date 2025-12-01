import requests
import json
import time

CACHE_FILE = "cache/hackerone.json"

def load_cache():
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def fetch_hackerone():
    """Fetches public programs from HackerOne."""
    url = "https://api.hackerone.com/v1/hackers/programs/"
    items = []

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            json_data = response.json()

            for program in json_data.get("data", []):
                attrs = program.get("attributes", {})
                items.append(attrs.get("name"))
    except Exception as e:
        print("Error fetching HackerOne:", e)

    return items
