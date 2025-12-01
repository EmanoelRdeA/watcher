import time
import yaml
from platforms.hackerone import fetch_hackerone_programs
from platforms.bugcrowd import fetch_bugcrowd_programs
from notify import notify

def load_config():
    with open("config.yml", "r") as f:
        return yaml.safe_load(f)

def load_cache(path):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or []
    except:
        return []

def save_cache(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f)

def check_platform(name, fetch_func, cache_file):
    print(f"[+] Checking {name}...")

    old = set(load_cache(cache_file))
    new = set(fetch_func())

    added = new - old

    if added:
        for program in added:
            notify(f"[{name.upper()}] New program detected: {program}")
        save_cache(cache_file, list(new))
        print(f"[+] {len(added)} new programs found on {name}!")
    else:
        print(f"[-] No new programs on {name}.")

def main():
    config = load_config()
    interval = config.get("check_interval", 3600)

    while True:
        if config["platforms"].get("hackerone"):
            check_platform("HackerOne", fetch_hackerone_programs, "cache/hackerone.json")

        if config["platforms"].get("bugcrowd"):
            check_platform("Bugcrowd", fetch_bugcrowd_programs, "cache/bugcrowd.json")

        print(f"[+] Sleeping for {interval} seconds...")
        time.sleep(interval)

if __name__ == "__main__":
    main()
