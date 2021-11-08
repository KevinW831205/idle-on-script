import pyautogui
import time

sampleX = 1650
sampleY = 700

while True:
    time.sleep(5)
    ## upper platform = (28, 20, 22)
    ## lower platform = (75, 63, 43)
    ss = pyautogui.screenshot(region=(sampleX, sampleY, sampleX + 1, sampleY + 1))
    r, g, b = ss.load()[0, 0]

    if r == 28:
        pyautogui.moveTo(100, 475)
        pyautogui.dragTo(1840, 475, 2, button='left')
    else:
        pyautogui.moveTo(100, 635)
        pyautogui.dragTo(1840, 635, 2, button='left')
