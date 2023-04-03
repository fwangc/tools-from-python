import pyautogui
import sys
import time
from datetime import datetime

numMin = None

print('We will keep you computer awake by moving the mouse every 1 minutes. ¯\_(ツ)_/¯')

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
     numMin = 1
else:
     numMin = int(sys.argv[1])

while True:
    pyautogui.moveRel(0, 20, duration=0.1)  # move mouse 20 pixels down
    pyautogui.moveRel(0, -20, duration=0.1)  # move mouse 20 pixels up
    print("Movement made at {}".format(datetime.now().time()))
    time.sleep(numMin*60)  # wait for numMin minute(s)