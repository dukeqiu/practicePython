import os,time
import pyautogui as pag

screenWidth, screenHeight = pag.size()
currentMouseX, currentMouseY = pag.position()

print(screenWidth, screenHeight)
print(currentMouseX,currentMouseY)
