#! /usr/bin/python

import time
import keyboard
import pyautogui
import threading

INTERVAL = 0.5          # Time interval between consecutive clicks
DELAY = 0.5             # Time delay between consecutive program cycles [after the clicks are turned off]
TOGGLE_KEY = 'shift'    # Key to toggle the clicking
EXIT_KEY = 'esc'        # Key to stop and exit from the program

class AutoClicker(threading.Thread):
    def __init__(self, interval, delay):
        super(AutoClicker, self).__init__()
        self.interval = interval
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def toggle_clicking(self):
        if self.running:
            self.stop_clicking()
        else:
            self.start_clicking()

    def click(self):
        width, height = pyautogui.position()
        pyautogui.click(width, height)

    # This function is invoked when the thread starts.
    def run(self):
        while self.program_running:
            while self.running:
                self.click()
                time.sleep(self.interval)
            time.sleep(self.delay)

if __name__ == '__main__':
    # Run indefinite loop of clicking on seperate thread
    auto_clicker_thread = AutoClicker(INTERVAL, DELAY)
    auto_clicker_thread.start()  # Invokes run() function of the thread

    # So that we can listen for key presses on the main thread
    keyboard.add_hotkey(TOGGLE_KEY, lambda: auto_clicker_thread.toggle_clicking())
    keyboard.add_hotkey(EXIT_KEY, lambda: auto_clicker_thread.exit())
