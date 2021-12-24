import pyautogui
import keyboard
import time
run = False

while True:
    time.sleep(0.5)
    if keyboard.is_pressed("v"):
        if not run:
            pyautogui.keyDown("shift")
            pyautogui.keyDown("w")
            pyautogui.mouseDown()
            run = not run

        elif run:
            pyautogui.keyUp("shift")
            pyautogui.keyUp("w")
            pyautogui.mouseUp()
            run = not run

        time.sleep(0.5)


