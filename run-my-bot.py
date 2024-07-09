#python3 script to start bot process Telebot_store
import sys
import psutil
#### BEGINNING ###
# my path
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
# Config import
from QRcodebot_cfg import *
# status
def filter_processes_by_port(bot_lport):
  filtered_processes = []
  pid_list = []
  for process in psutil.process_iter():
    try:
      # Check connections for the desired port
      for connection in process.connections():
        if connection.laddr.port == bot_lport:
          filtered_processes.append(process)
          break  # Stop iterating connections if found
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass  # Handle potential exceptions
  pid_list = [process.pid for process in filtered_processes] 
  return filtered_processes, pid_list
# Now you can use the pid_list in your kill_processes function
def kill_processes(pid_list):
    for pid in pid_list:
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait(timeout=3)  # Wait for the process to terminate
            print(f"Successfully terminated process {pid}")
        except psutil.NoSuchProcess:
            print(f"No such process: {pid}")
        except psutil.AccessDenied:
            print(f"Access denied: {pid}")
        except psutil.TimeoutExpired:
            print(f"Timeout expired for process {pid}")
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
