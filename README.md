Here’s the improved guide in markdown format:

```markdown
# QRcode-bot
### QR Code Generator (Telegram Bot)

## Introduction
This guide will teach you how to set up your Telegram bot, which generates an A4 PDF for your custom web link (URL) with a custom title (can be Cyrillic).

## Requirements
- Python 3.11
- MySQL 8
- Existing Telegram bot token (can be obtained from [@BotFather](https://t.me/botfather))

## Setup

1. Place all bot files in a user folder on your dedicated web server.
2. Import the database by running:
   ```sh
   mysql QRcodebot_cfg.sql
   ```
3. Copy `QRcodebot_cfg_example.py` to `QRcodebot_cfg.py` and insert your credentials.
4. Set the Telegram Web Hook by running:
   ```sh
   python bot_manage_webhook.py
   ```
   (It is recommended to use Nginx for proxying bot traffic.)
5. Run the Bot:
   ```sh
   python run-my-bot.py start
   ```
6. Start using your bot!
