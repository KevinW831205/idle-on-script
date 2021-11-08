import pyautogui
import time

while True:
    time.sleep(5)
    pyautogui.moveTo(100, 810)
    pyautogui.dragTo(1840, 810, 2, button='left')
