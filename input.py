#!/usr/bin/python3
# possible modules:
# 	pyautogui keyboard
from pyautogui import keyUp, keyDown, typewrite, press, click, size
from time import sleep
from os import system

w, h = size()
print(w,h)
click(100,100)
keyDown('w')

while True:
	keyDown('enter')
	keyUp('enter')



