import pyautogui
import time

points = [(70, 430, 1795, 430), (785, 510, 1795, 510)]


while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')