import pyautogui
import time

pointsBot = [(400, 200, 1500, 200), (70, 570, 1100, 570), (490, 650, 1780, 650)]
pointsTop = [(340, 480, 1260, 480)]

while True:
    time.sleep(5)
    for x1, y1, x2, y2 in pointsBot:
        t = (x2 - x1)/500
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, t, button='left')