import pyautogui
import time

points = [(70, 590, 1795, 590), (630, 690, 1485, 690), (70, 795, 1010, 795)]


while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')