#python3 script to start bot process Telebot_store
import sys
#### BEGINNING ###
# my path
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
# Config import
from QRcodebot_cfg import *
# Help message
if len(sys.argv) == 1:
    print("Usage: {} [start|stop|status]".format(sys.argv[0]))
    sys.exit(1)
pids_tokill = []
# Start, stop, or check status of Gunicorn
action = sys.argv[1]
if action == "start":
    filtered_processes, pids_tokill = filter_processes_by_port(bot_lport)
    if filtered_processes:
        print ("Bot is already running.")
    else:
        psutil.Popen(
        ["gunicorn",
         "-b", "localhost:{}".format(bot_lport),
         "-w", "4",
         "-t", "180",
         "--log-file={}".format(logfpath),
         "QRcodebot:app",
         "--chdir", script_directory]
        )
        print("Bot started.")
elif action == "stop":
    filtered_processes, pids_tokill = filter_processes_by_port(bot_lport)
    if pids_tokill:
        kill_processes(pids_tokill)
    else:
        print ("Bot is not running.")
elif action == "status":
    # Show the status of Gunicorn processes
    filtered_processes, pids_tokill = filter_processes_by_port(bot_lport)
    if filtered_processes:
        print(filtered_processes)
    else:
        print ("Telebot_store is not running.")
else:
    print("Usage: {} [start|stop|status]".format(sys.argv[0]))
    sys.exit(1)
