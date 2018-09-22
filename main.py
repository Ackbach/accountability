# For arguments to PyQt5 QApplication class.
import sys
# Need for build?
import encodings

# For ini file parser.
import configparser

# For screen capture.
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QApplication

# For generating filename: randint(0, 59)
from random import randint
import os

# datetime.datetime.now() gets the current time.
import datetime
import time

# Debug flag:
debug_flag = True
# impordebug_flag = False

# Set up QApplication for screen capture.
app = QApplication(sys.argv)
screen = QGuiApplication.primaryScreen()

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

    # Ready to take the screenshot.
    desktop_pixmap = screen.grabWindow(0)

    # Build the filename.
    the_time = datetime.datetime.now()
    if debug_flag:
        print('The current time is: ' +
              the_time.strftime('%Y-%m-%d %H.%M.'))

    # Filename will be: YYYY-MM-DD hh.mm.computer_name.png
    file_name = the_time.strftime('%Y-%m-%d %H.%M.') + computer_name \
        + '.png'
    if debug_flag:
        print('The file name generated is: ' + file_name)

    # Now get the full path:
    file_path = os.path.join(target_folder, file_name)
    if debug_flag:
        print('The full file path generated is: ' + file_path)

    # Save file.
    desktop_pixmap.save(file_path)

    # Initialize the random minute
    minute_to_sleep = randint(0, 59)
    if debug_flag:
        print('Minutes to sleep: ' + str(minute_to_sleep))

    time.sleep(minute_to_sleep * 60)
