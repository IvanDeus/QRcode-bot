# script to configure webhook for a bot
import requests
import argparse
# Config import
from QRcodebot_cfg import *

def set_telegram_webhook(token, url, max_connections=28, drop_pending_updates=True):
    telegram_api_url = f"https://api.telegram.org/bot{token}/setWebhook"
    payload = {
        'url': url,
        'max_connections': max_connections,
        'drop_pending_updates': drop_pending_updates
    }
    response = requests.post(telegram_api_url, data=payload)
    return response.json()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set Telegram webhook.')
    parser.add_argument('url', type=str, help='Webhook URL')
    args = parser.parse_args()
    response = set_telegram_webhook(main_bot_token, args.url)
    print(response)
