# QRcode-bot
QR code generator (Telegram bot)

## Intro
This instruction will teach you how to set up your telegram bot which generates A4 pdf for your custom web link (URL) 

## Requirements: 
Python 3.11, MySQL 8. Existing Telegram bot token (can be obtained from @botfather).

## Set up

1. Place all bot files in a publicly accessible folder within your web server.
2. import database by using # mysql QRcodebot_cfg.sql 
3. copy QRcodebot_cfg_example.py to QRcodebot_cfg.py and insert your credentials in 
4. Set Telegram Web Hook: # python bot_manage_webhook.py  (It is recommended to use Nginx for proxying bot traffic)
5. Run the Bot: # python run-my-bot.py start
7. Start using you bot!

