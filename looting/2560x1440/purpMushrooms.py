import pyautogui
import time

points = [(470, 935, 1520, 935), (1470, 800, 2450, 800)]

while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')