# For arguments to PyQt5 QApplication class.
import sys
# Need for build?
# import encodings

# For ini file parser.
import configparser

# For screen capture.
from mss import mss

# For generating filename: randint(0, 59)
from random import randint
import os

# datetime.datetime.now() gets the current time.
import datetime
import time

# Debug flag:
debug_flag = True
# debug_flag = False

# Get data from ini file.
config = configparser.ConfigParser()
config.read('settings.ini')

# Get destination folder.
target_folder = config['Paths']['path_to_destination_folder']
if debug_flag:
    print('The target folder is ' + target_folder)

# Get computer name.
computer_name = config['Paths']['computer_name']
if debug_flag:
    print('The computer name is ' + computer_name)

# Outer loop just keeps the application going, period:
while True:

    # Build the filename.
    the_time = datetime.datetime.now()
    if debug_flag:
        print('The current time is: ' +
              the_time.strftime('%Y-%m-%d %H.%M.'))

    # Filename will be: YYYY-MM-DD hh.mm.computer_name.png
    pre_file_name = the_time.strftime('%Y-%m-%d %H.%M.') + computer_name
    if debug_flag:
        print('The prefix file name generated is: ' + pre_file_name)

    file_name = pre_file_name + '.png'
    file_path = os.path.join(target_folder, file_name)
        
    with mss() as sct:
        sct.compression_level = 3
        sct.shot(mon=-1, output=file_path)

    # Initialize the random minute
    minute_to_sleep = randint(1, 60)
    if debug_flag:
        print('Minutes to sleep: ' + str(minute_to_sleep))

    time.sleep(minute_to_sleep * 60)
