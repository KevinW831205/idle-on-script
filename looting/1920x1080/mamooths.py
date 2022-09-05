import pyautogui
import time

points = [(600, 575, 1500, 575), (90, 285, 980, 285), (980, 360, 1710, 360)]
points1 = [(600, 755, 1500, 755), (90, 480, 980, 480), (980, 560, 1710, 560)]


while True:
    time.sleep(5)
    for x1, y1, x2, y2 in points:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')