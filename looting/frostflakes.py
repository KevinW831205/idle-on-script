import pyautogui
import time

points = [(780, 607, 1450, 607), (90, 467, 770, 467), (640, 275, 1484, 275)]

while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')