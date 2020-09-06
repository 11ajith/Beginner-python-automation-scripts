# Move the mouse pointer to avoid screen off

import time
import pyautogui


def make_busy():
    print('Press CTRL-C to stop.')
    try:
        while True:
            pyautogui.moveRel(25, 0, 0.5)
            pyautogui.moveRel(-25, 0, 0.5)
            time.sleep(5)
    except KeyboardInterrupt:
        print('Process has stopped')

make_busy()