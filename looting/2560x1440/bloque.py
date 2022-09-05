import pyautogui
import time

points = [(70, 725, 2000, 725), (1130, 875, 1525, 875), (90, 1045, 2125, 1045)]

while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')