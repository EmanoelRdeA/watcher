import requests
import yaml

def load_config():
    with open("config.yml", "r") as f:
        return yaml.safe_load(f)

config = load_config()

def notify(message):
    if config["notify"]["telegram"]["enabled"]:
        send_telegram(message)

    if config["notify"]["discord"]["enabled"]:
        send_discord(message)


def send_telegram(message):
    token = config["notify"]["telegram"]["token"]
    chat_id = config["notify"]["telegram"]["chat_id"]

    if not token or not chat_id:
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram error:", e)


def send_discord(message):
    webhook = config["notify"]["discord"]["webhook_url"]

    if not webhook:
        return

    data = {"content": message}

    try:
        requests.post(webhook, json=data)
    except Exception as e:
        print("Discord error:", e)
