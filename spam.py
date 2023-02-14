import pyautogui
import time

limit = input("Enter limit:")
message = input("Enter message:")
i = 0
time.sleep(5)

while i < int(limit):
    pyautogui.typewrite(message)
    pyautogui.press("enter")

    i+=1