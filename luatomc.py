import pydirectinput
import pyperclip
import time

f = open('luacode.txt','r')
print("Writing in 5...")
time.sleep(1)
print("Writing in 4...")
time.sleep(1)
print("Writing in 3...")
time.sleep(1)
print("Writing in 2...")
time.sleep(1)
print("Writing in 1...")
time.sleep(1)
for line in f:
    if line[:-1] == 'BACKSPACE!':
        pydirectinput.press('backspace')
    else:
        pyperclip.copy((line[:-1]))
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('v')
        pydirectinput.keyUp('ctrl')
        pydirectinput.press('enter')
    time.sleep(0.01)
print("DONE")