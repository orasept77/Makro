import pyautogui
import time

a = ['3090','2799','3004','4294','4097','3002','3948','3904','4064', '4334','4720','4693','4503','4503','6327']
it = iter(a)
while True:
    try:
        asd = next(it)
        pyautogui.PAUSE = 1.5
        pyautogui.moveTo(x=-1645, y=309)
        pyautogui.click(clicks=2)
        pyautogui.write(asd)
        pyautogui.press("enter")
        pyautogui.moveTo(x=-1409, y=522)
        pyautogui.click()
        pyautogui.moveTo(x=-1545, y=440)
        pyautogui.click()
        pyautogui.PAUSE = 0.8
        pyautogui.moveTo(x=-1182, y=492)
        pyautogui.click()
        pyautogui.moveTo(x=-701, y=1009)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=-1645, y=301)
        pyautogui.click(clicks=2)
    except:
        break