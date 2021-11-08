import pyautogui
import time

sampleX = 180
sampleY = 130
# pyautogui.moveTo(sampleX, sampleY)
print(pyautogui.position())
# x,y = pyautogui.position()
#

#TOP: 87 72 65
#

# ss = pyautogui.screenshot(region=(sampleX, sampleY, sampleX + 1, sampleY + 1))
# r,g,b = ss.load()[0, 0]
# print((r, g, b))

# for y in range(400, 850):
#     pyautogui.moveTo(1650, y)
#     ss = pyautogui.screenshot(region=(1650,y, 1651, y+1))
#     print(ss.load()[0,0])