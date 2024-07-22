import time
import pyautogui
import random

def screenshot():
    name=random.randint(1,100)
    name='{}.png'.format(name)
    time.sleep(4)
    img=pyautogui.screenshot(name)
    img.show()

screenshot()