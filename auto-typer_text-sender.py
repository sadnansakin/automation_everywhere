import pyautogui
import time
import webbrowser

time.sleep(3)

print("Are you ready? Type: yes or no")
take_input = input()

time.sleep(1)

if take_input == "yes":
    print("please open your app and and click on type a message box")
    time.sleep(2)
    while True:
        pyautogui.typewrite("valo hoye jao tomra")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(0.1)

elif take_input == "no":
    #pyautogui.hotkey('ctrl','c')
    quit() # quit() is for exit a python program.



