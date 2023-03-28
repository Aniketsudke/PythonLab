from itertools import count
from socket import has_ipv6
import pyautogui
import time
time.sleep(4)
count = 0
while count<=100:
    pyautogui.typewrite("No")
    pyautogui.press("enter")
    count = count + 1
