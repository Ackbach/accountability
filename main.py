# For arguments to PyQt5 QApplication class.
import sys
# Need for build?
# import encodings

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

    # Set up QApplication for screen capture.
    app = QApplication(sys.argv)
    screens = QGuiApplication.screens()
    if 1 < len(screens):
        for i in range(len(screens)):
            file_name = pre_file_name + '.Mon-' + str(i) + '.png'

            # Now get the full path:
            file_path = os.path.join(target_folder, file_name)
            if debug_flag:
                print('The full file path generated is: ' + file_path)

            screens[i].grabWindow(0).save(file_path)

    else:
        file_name = pre_file_name + '.png'
        file_path = os.path.join(target_folder, file_name)
        if debug_flag:
            print('The full file path generated is: ' + file_path)
        screens[0].grabWindow(0).save(file_path)

    # Tear down all classes. If monitors change, this should be ok.
    del screens
    del app

    # Initialize the random minute
    minute_to_sleep = randint(0, 59)
    if debug_flag:
        print('Minutes to sleep: ' + str(minute_to_sleep))

    time.sleep(minute_to_sleep * 60)
