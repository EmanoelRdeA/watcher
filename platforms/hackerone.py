import requests

def fetch_hackerone_programs():
    url = "https://hackerone.com/programs/search.json?query=type:hackerone&sort=published_at:desc"

    try:
        data = requests.get(url).json()
        programs = [p["name"] for p in data.get("results", [])]
        return programs
    except Exception as e:
        print("HackerOne error:", e)
        return []
