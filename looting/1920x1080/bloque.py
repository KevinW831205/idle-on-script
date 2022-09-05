import pyautogui
import time

points = [(75, 540, 1500, 540), (830, 660, 1170, 660), (75, 775, 1550, 775)]

while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')