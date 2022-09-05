import pyautogui
import time

points = [(70, 820, 2470, 820), (70, 1070, 1425, 1070)]


while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')