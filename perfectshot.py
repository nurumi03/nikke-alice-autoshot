from pynput import keyboard
import time
import interception
import os
from random import uniform
import json

# abs_dir = os.path.dirname(os.path.abspath('__file__'))
# app_dir = os.environ.get('SYSTEMDRIVE') + os.path.sep + 'perfectshot'

config_path = os.path.join(app_dir, 'config.json')

with open(config_path, 'r') as file:
    config = json.load(file)

CHARACTER = config['nikke']['character']
MOUSE_BUTTON = config['nikke']['mouse_button']
SLEEP_START = config['nikke']['sleep_start']
SLEEP_END = config['nikke']['sleep_end']
SLEEP_MODIFIER = 0

interception.auto_capture_devices()


stop_loop = False


def on_press(key):
    global stop_loop
    try:
        if key == keyboard.Key.cmd:
            stop_loop = True
            return False
    except AttributeError:
        pass


# Listener used to stop the click loop
listener = keyboard.Listener(on_press=on_press)
listener.start()


def sleep(start=0.3, end=0.7, modifier=SLEEP_MODIFIER):
    time.sleep(uniform(start, end) + modifier)


def rapid_shot():
    while not stop_loop:
        print(f'{CHARACTER} is shooting!')
        interception.mouse_down(MOUSE_BUTTON)
        sleep(SLEEP_START, SLEEP_END)
        interception.mouse_up(MOUSE_BUTTON)


# I'm compile with this command
# pyinstaller --onefile --noconsole --distpath C:\perfectshot --workpath C:\perfectshot\build --specpath C:\perfectshot\spec .\perfectshot.py

rapid_shot()
