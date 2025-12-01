import requests

def fetch_bugcrowd_programs():
    url = "https://bugcrowd.com/programs.json"

    try:
        data = requests.get(url).json()
        programs = [p["name"] for p in data.get("programs", [])]
        return programs
    except Exception as e:
        print("Bugcrowd error:", e)
        return []
