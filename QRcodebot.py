# QR code generator by Ivan Deus for Telegram
#
#
#telebot store Ivan Deus
from flask import Flask, request, jsonify, render_template, redirect, url_for, make_response, abort
import json
import time
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
# Function to add or update a user in the 'telebot_users' table
def add_or_update_user(chat_id, name, message, conn, first_name, last_name):
    try:
        with conn.cursor() as cursor:
            # Convert chat_id to a string and then escape it to prevent SQL injection
            chat_id_str = conn.escape_string(str(chat_id))
            name = conn.escape_string(name)
            message = conn.escape_string(message)
            first_name = conn.escape_string(first_name)
            last_name = conn.escape_string(last_name)
            # Check if the user already exists in the table
            query = f"SELECT * FROM telebot_users WHERE chat_id = '{chat_id_str}'"
            cursor.execute(query)
            if cursor.rowcount > 0:
                # User exists, update the record
                update_query = f"UPDATE telebot_users SET lastmsg = '{message}' WHERE chat_id = '{chat_id_str}'"
                cursor.execute(update_query)
            else:
                # User does not exist, insert a new record
                insert_query = f"INSERT INTO telebot_users (chat_id, name, lastmsg, first_name, last_name, Sub) VALUES ('{chat_id_str}', '{name}', '{message}', '{first_name}', '{last_name}', 1)"
                cursor.execute(insert_query)
            # Commit the changes to the database
            conn.commit()
    except pymysql.Error as e:
        # Handle any database errors here
        print(f"Database error: {e}")



##########
# Main bot logic
@app.route('/webhook', methods=['POST'])
def telebothook1x():
    try:
        conn = connect_to_mysql()
        #V2 Get update array
        json_string = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_string)
        bot = telebot.TeleBot(telebot_vars['main_bot_token'])
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
            keys_start = "(Gen QRcode, /qr, Help, /help)"
            # add user to database
            add_or_update_user(chat_id, name, message.text, conn, first_name, last_name)
            if message.text == '/start':
                #just send a start message
                bot.send_message(chat_id, "QR code generator", reply_markup=keys_start, parse_mode='html')
            else:
                bot.send_message(chat_id, "Sorry, I don't understand", reply_markup=keys_start, parse_mode='html')
        # do call backs   
        elif update.callback_query is not None:
            calld = update.callback_query.data
            chat_id = update.callback_query.message.chat.id
            if calld == '/qr':
                bot.send_message(chat_id, "Type URL", reply_markup=keys_start, parse_mode='html')
            elif calld.startswith("https"):
                bot.send_message(chat_id, "Type title", reply_markup=keys_start, parse_mode='html')
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
