# QR code generator by Ivan Deus for Telegram
#
#
#telebot store Ivan Deus
from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response, abort
import user_agents
import json
import re
import time
from passlib.hash import pbkdf2_sha256
import telebot
from telebot import types
#### BEGINNING ###
# my path
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
# Config import
from QRcodebot_cfg import *
# start web service
app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# ... Route Code begins
conn = None
# Create a database connection with Unix socket
def connect_to_mysql():
    try:
        conn = pymysql.connect(unix_socket=mysql_unix_socket, user=db_username, password=db_password, database=db_name)
        return conn
    except pymysql.err.OperationalError as err:
        print(f"Error connecting to MySQL server: {err}")
        return None 


##########
# Main bot logic
@app.route('/webhook', methods=['POST'])
def telebothook1x():
    try:
        conn = connect_to_mysql()
        telebot_vars = fetch_telebot_vars_into_dict(conn)
        #V2 Get update array
        json_string = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_string)
        bot = telebot.TeleBot(telebot_vars['main_bot_token'])
        keys_welcome = inline_button_constructor(f"{telebot_vars['welcome_keys']}, /categories")
        keys_start = inline_button_constructor((get_prods_category(conn)))
        # Access name and chat_id only when there is a message
        if (update.message is not None) and (update.message.text is not None):
            message = update.message
            if message.chat.username:
                name = message.chat.username
            else:
                name = ' '
            # find first name
            first_name = message.chat.first_name
            if message.chat.last_name:
                last_name = message.chat.last_name
            else:
                last_name = ' '
            chat_id = message.chat.id
            # add user to database
            add_or_update_user(chat_id, name, message.text, conn, first_name, last_name)
            if message.text == '/start':
                # let us begin
                try:
                    with open(script_directory+'/static/' + telebot_vars['welcome_banner'], 'rb') as photo:
                        bot.send_photo(chat_id, photo)
                except FileNotFoundError:
                    print ("No welcome banner")
                #just send a start message
                bot.send_message(chat_id, telebot_vars['welcome_message'], reply_markup=keys_start, parse_mode='html')
            else:
                bot.send_message(chat_id, telebot_vars['welcome_nostart'], reply_markup=keys_welcome, parse_mode='html')
        # do call backs         
        elif update.callback_query is not None:
            calld = update.callback_query.data
            chat_id = update.callback_query.message.chat.id
            if calld == '/categories':
                bot.send_message(chat_id, telebot_vars['welcome_message'], reply_markup=keys_start, parse_mode='html')
            elif calld.startswith("https_"):
                prodidx = re.sub(r'https_', '', calld)
                order_placed = order_placed_in_store(conn, chat_id, prodidx)
                if order_placed:
                    bot.send_message(chat_id, telebot_vars['buy_text'] + order_placed, reply_markup=keys_welcome, parse_mode='html')
            else:
                products = get_prods_for_category(conn, calld)
                for product in products:
                    with open(script_directory+'/static/' + product[2], 'rb') as photo:
                        bot.send_photo(chat_id, photo, caption=product[1])
                    keys_prod = inline_button_constructor(f"{telebot_vars['buy_button']}, https_{product[0]}, {telebot_vars['welcome_keys']}, /categories")
                    bot.send_message(chat_id, product[3], reply_markup=keys_prod, parse_mode='html')        
    finally:
        # Close the database connection
        if conn:
            conn.close()
    # If there's no message to handle, return an empty response
    return '', 204  # HTTP 204 No Content
# start constant loop with open connection
if __name__ == '__main__':
    # Change the host and port here
    app.run(host='127.0.0.1', port=bot_lport)
