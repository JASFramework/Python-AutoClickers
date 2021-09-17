#! /usr/bin/python

import pyautogui
import time 
import keyboard
import threading

# The Switch
on_off = False 

# This function does the clicking
def Auto_Click():
    width, height = pyautogui.position()
    pyautogui.click(width, height)
    time.sleep(0.5)
    
def check_press():
    global on_off
    if keyboard.is_pressed('s') and on_off:
        on_off = False
        print("Auto Clicker Killed")
    elif keyboard.is_pressed('r') and not on_off:
        on_off = True
        print("Auto Clicker Restarted")
    time.sleep(0.1) #Check every 10th of a second
    check_press()

check_thread = threading.Thread(target = check_press)
check_thread.start()

# Checks if you hit the kill button. If you did not hit the kill button, run the Auto_Click function. 
while True:
    while on_off == True:
      Auto_Click()
