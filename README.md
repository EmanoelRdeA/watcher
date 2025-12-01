Hello, there... Been working on an automated notification system for HackerOne and Bugcrowd program updates, with alerts sent to Telegram and Discord.
This tool helps security researchers stay up-to-date when new bug bounty programs appear or existing ones change.

## Features
Fetches bug bounty programs from:
HackerOne
Bugcrowd

## Sends notifications to:
Telegram Bot
Discord Webhook

Keeps a local cache to avoid duplicate alerts
Fully configurable via config.yml
Easy to extend — add new platforms in platforms/

### Installation 

git clone https://github.com/EmanoelRdeA/watcher

cd watcher

## Install dependencies

pip install -r requirements.txt

### Configuration
Edit -> config.yml 

Ex:

telegram:
  token: "YOUR_TELEGRAM_BOT_TOKEN"
  chat_id: "YOUR_CHAT_ID"

discord:
  webhook_url: "YOUR_DISCORD_WEBHOOK"
interval: 60   # check every 60 seconds 

## Telegram Setup

Open Telegram and search BotFather

Run /start
Run /newbot → get your bot token
Start a chat with your bot

Get your chat ID via:
https://api.telegram.org/bot
<YOUR_TOKEN>/getUpdates
Add both values to config.yml

## Discord setup

Go to your server
Server Settings → Integrations → Webhooks
Create a new webhook
Copy the URL
Place it in config.yml
