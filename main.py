# For ini file parser.
import configparser

# For screen capture.
from mss import mss

# For generating filename: randint(1, 60)
from random import randint
import os

# datetime.datetime.now() gets the current time.
import datetime
import time

# Debug flag:
debug_flag = False

# Get data from ini file.
config = configparser.ConfigParser()
config.read('settings.ini')

# Get destination folder.
target_folder = config['Paths']['path_to_destination_folder']
print('The target folder is ' + target_folder)

# Get computer name.
computer_name = config['Paths']['computer_name']
print('The computer name is ' + computer_name)

time_format = '%Y-%m-%d %H.%M.%S.'
time_only_format = '%H.%M.%S.'
file_path = ''
one_week = datetime.timedelta(weeks=1)

first_run = True

# Outer loop just keeps the application going, period:
while True:

    the_time = datetime.datetime.now()

    if debug_flag:
        print('The current time is: ' +
              the_time.strftime(time_format))

    if not first_run:

        # Rename the previous file to include time range
        last_file_path = file_path
        rename_file_path = last_file_path.split('.' + computer_name)[0]
        rename_file_path += ' to ' + the_time.strftime(time_only_format)
        rename_file_path += computer_name + '.png'
        os.rename(last_file_path, rename_file_path)

    # Filename will be: YYYY-MM-DD hh.mm.ss.computer_name.png
    pre_file_name = the_time.strftime(time_format) + computer_name
    if debug_flag:
        print('The prefix file name generated is: ' + pre_file_name)

    # Build full file path.
    file_name = pre_file_name + '.png'
    file_path = os.path.join(target_folder, file_name)

    # Grab the screenshot. The mon=-1 grabs all monitors, and the
    # compression_level = 3 makes the files smaller. They're still
    # quite viewable.
    with mss() as sct:
        sct.compression_level = 3
        sct.shot(mon=-1, output=file_path)

    # Now delete files older than a week.

    # List the files in the target folder.
    files = os.listdir(target_folder)

    # Filter down to just pictures we've put there. Filename should
    # start with four numbers and end in '.png'.
    files = [file for file in files
             if (str(file)[0].isdigit()
                 and str(file)[1].isdigit()
                 and str(file)[2].isdigit()
                 and str(file)[3].isdigit()
                 and str(file).endswith('.png'))]

    # Grab the dates of the files for comparison.
    dates = [datetime.datetime.strptime(file[:19], time_format[:-1])
             for file in files]

    # Now filter down to just those dates that are more than one week
    # prior.
    dates = [dt for dt in dates if the_time - one_week >= dt]

    delete_files = []
    for dt in dates:
        for file in files:
            if str(file).startswith(dt.strftime(time_format[:-1])):
                delete_files.append(file)

    # Loop through the files. If a file starts with a date in dates,
    # delete it.
    for file in delete_files:
        os.remove(os.path.join(target_folder, file))

    # Initialize the random minute
    minute_to_sleep = randint(1, 60)
    if debug_flag:
        print('Minutes to sleep: ' + str(minute_to_sleep))

    # Sleep an undisclosed amount of time.
    time.sleep(minute_to_sleep * 60)

    first_run = False
