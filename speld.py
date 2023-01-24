import time
import turtle
import pyautogui

a = ["U MI 220W MMA", "U I THF220SAC", "U MI 220AL CU","MIG","P K MA JWS-A35","Weldman mig 200","U MI 208ALDII"]
it = iter(a)
while True:
    try:
        time.sleep(2)
        pyautogui.PAUSE = 0.5
        asd = next(it)
        pyautogui.moveTo(x=-1485, y=294)


    except:
        break
