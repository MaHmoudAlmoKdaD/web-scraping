import pyautogui as gy
import time

print("Script will running in 5 Seconds...\nChoose your page you want to control on the textBox!")
time.sleep(5)

for i in range(2):
    gy.write("write what you want to send...")
    gy.press("Enter")