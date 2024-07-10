# QRcode-bot
### QR Code Generator (Telegram Bot)

## Introduction
This guide will walk you through setting up your Telegram bot, which generates an A4 PDF containing a QR code for your custom web link (URL) with a custom title (including Cyrillic characters).

## Requirements
- Python 3.11
- MySQL 8
- A Telegram bot token (obtainable from [@BotFather](https://t.me/botfather))

## Setup Instructions

1. **Organize Bot Files**: Place all bot files in a user directory on your dedicated web server.
2. **Import Database**: Run the following command to import the database configuration:
   ```sh
   mysql < QRcodebot_cfg.sql
   ```
3. **Configure Credentials**: Copy `QRcodebot_cfg_example.py` to `QRcodebot_cfg.py` and insert your credentials.
4. **Set Telegram Webhook**: Run the following command to set the Telegram Webhook:
   ```sh
   python bot_manage_webhook.py
   ```
   (It is recommended to use Nginx for proxying bot traffic.)
5. **Start the Bot**: Execute the following command to run your bot:
   ```sh
   python run-my-bot.py start
   ```
6. **Begin Usage**: Your bot is now ready to use!
