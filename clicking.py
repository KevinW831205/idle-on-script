import pyautogui
import time

# sampleX = 180
# sampleY = 130
# pyautogui.moveTo(sampleX, sampleY)
# x,y = pyautogui.position()
#
mouse_X, mouse_Y = pyautogui.position()
print(mouse_X, mouse_Y)

# start = time.time()
# pixel = pyautogui.screenshot(
#     region=(
#         mouse_X, mouse_Y, 1, 1
#     )
# )
# color = pixel.getcolors()
# print(color)
# print(time.time() - start)
#TOP: 87 72 65
#


# ss = pyautogui.screenshot(region=(sampleX, sampleY, sampleX + 1, sampleY + 1))
# r,g,b = ss.load()[0, 0]
# print((r, g, b))

# for y in range(400, 850):
#     pyautogui.moveTo(1650, y)
#     ss = pyautogui.screenshot(region=(1650,y, 1651, y+1))
#     print(ss.load()[0,0])

# while True:
#     (sampleX, sampleY) = pyautogui.position()
#     ss = pyautogui.screenshot(region=(sampleX, sampleY, sampleX + 1, sampleY + 1))
#     r,g,b = ss.load()[0, 0]
#     print((r, g, b))
#     if r != 16:
#         pyautogui.click()
#         break
