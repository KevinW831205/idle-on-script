import pyautogui
import time

points = [(1230, 755, 60, 755), (180, 385, 1000, 385)]

while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = abs((x2 - x1)/500)
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')