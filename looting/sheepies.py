import pyautogui
import time

sampleX = 1650
sampleY = 700

heights = [470, 600, 710, 810]

while True:
    time.sleep(5)
    for y in heights:
        pyautogui.moveTo(100, y)
        pyautogui.dragTo(1840, y, 2, button='left')
