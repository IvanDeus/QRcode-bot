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
#QR import
import qrcode
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
#QR gen
def generate_qr_code_with_pdf(url, output_image_file, output_pdf_file, caption):
    """
    Generates a QR code for a given URL, saves it as a PNG file, and creates an A4 PDF file
    with a caption above the QR code.
    """
    output_image_file = script_directory +'/static/'+ output_image_file
    output_pdf_file = script_directory +'/static/'+ output_pdf_file
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
  
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image
    img.save(output_image_file)
    # Create PDF
    c = canvas.Canvas(output_pdf_file, pagesize=A4)
    # Set up dimensions
    width, height = A4
    # Set caption font size and center alignment
    #pdfmetrics.registerFont(TTFont('Helvetica Cyrillic', script_directory+'/static/'+'Helvetica Cyrillic.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans', script_directory+'/static/'+'DejaVuSans.ttf'))
    caption_font_size = 36
    c.setFont("DejaVuSans", caption_font_size)
    c.setFillColor(HexColor("#800080"))  # Deep purple color
    caption_width = c.stringWidth(caption, "DejaVuSans", caption_font_size)
    # Add caption Positions center h and x inches below the top of the page.
    c.drawString((width - caption_width) / 2, height - 1.6*inch, caption)
    # Add QR code image
    qr_code_size = 6*inch  # Increase the size of the QR code
    c.drawImage(output_image_file, (width - qr_code_size) / 2, height - 8*inch, qr_code_size, qr_code_size)
    # Save the PDF
    c.showPage()
    c.save()


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
# get text for buttons etc
def fetch_telebot_vars_into_dict(conn):
    try:
        with conn.cursor() as cursor:
            query = "SELECT param, value FROM telebot_vars"
            cursor.execute(query)
            result = cursor.fetchall()
            telebot_vars = {}  # Initialize an empty dictionary
            for row in result:
                param, value = row
                telebot_vars[param] = value  # Add data to the dictionary
            return telebot_vars
    except pymysql.Error as e:
        # Handle any database errors here
        print(f"Database error: {e}")
        return {}
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
        telebot_vars = fetch_telebot_vars_into_dict(conn)
        #V2 Get update array
        json_string = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_string)
        bot = telebot.TeleBot(main_bot_token)
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
            # form buttons
            keys_start = "(Gen QRcode, /qr, Help, /help)"
            # add user to database
            add_or_update_user(chat_id, name, message.text, conn, first_name, last_name)
            if message.text == '/start':
                #just send a start message
                bot.send_message(chat_id, telebot_vars['welcome_message'], reply_markup=keys_start, parse_mode='html')
            else:
                bot.send_message(chat_id, telebot_vars['welcome_nostart'], reply_markup=keys_start, parse_mode='html')
        # do call backs   
        elif update.callback_query is not None:
            calld = update.callback_query.data
            chat_id = update.callback_query.message.chat.id
            if calld == '/qr':
                bot.send_message(chat_id, telebot_vars['url'], reply_markup=keys_start, parse_mode='html')
            elif calld.startswith("https"):
                bot.send_message(chat_id, telebot_vars['titul'], reply_markup=keys_start, parse_mode='html')
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
