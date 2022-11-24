import pyautogui
import time

#print(pyautogui.size())  #разрешение экрана общее

#pyautogui.PAUSE = 2.5

#print(pyautogui.position())  # Текущее положение мыши
#currentMouseX, currentMouseY = pyautogui.position()

#a = [4564,3090,2799,3004,4294,4097,3002,3948,3904,4064,4334,4720,4693,4503,4503,6327]
#time.sleep(5)
#distance = 200
#while distance > 0:
#        pyautogui.drag(distance, 0, duration=0.5)   # move right
#        distance -= 5
#        pyautogui.drag(0, distance, duration=0.5)   # move down
#        pyautogui.drag(-distance, 0, duration=0.5)  # move left
#        distance -= 5
#        pyautogui.drag(0, -distance, duration=0.5)  # move up

#import pyautogui as py #Import pyautogui
#import time #Import Time
#a = [4564,3090,2799,3004,4294,4097,3002,3948,3904,4064,4334,4720,4693,4503,4503,6327]
#while True:  # Start loop
#              print(py.position())
#              time.sleep(5)

#=============================================================================
#Chrome size 90%
a = ['2661','4766','3591','4766','4690','2938','2200','6109','6111','6225','6224','4900','2993','2938','4690']
it = iter(a)  # создаём итератор из списка
while True:
    try:
        asd = next(it)
        pyautogui.PAUSE = 0.7
        pyautogui.moveTo(x=-1621, y=311) #строка ввода
        time.sleep(2)
        pyautogui.click(clicks=2)
        pyautogui.write(asd)
        pyautogui.press('enter')
        pyautogui.moveTo(x=-1652, y=524)
        pyautogui.click()
        pyautogui.moveTo(x=-1431, y=467)
        pyautogui.click()
        pyautogui.write('promo')
        pyautogui.moveTo(x=-1422, y=519)
        pyautogui.click()
        pyautogui.moveTo(x=-1415, y=557)
        pyautogui.click()
        pyautogui.moveTo(x=-1214, y=561)
        pyautogui.click()
        pyautogui.moveTo(x=-1122, y=734)
        pyautogui.click()  # остановись на дате 24.11 число
        pyautogui.moveTo(x=-1093, y=743)
        pyautogui.click()    #Klika na 25
        # pyautogui.moveTo(x=-1162, y=603)
        # pyautogui.click()
        # pyautogui.moveTo(x=-1206, y=648)
        # pyautogui.click()promo
        pyautogui.moveTo(x=-1199, y=660)
        pyautogui.click()
        pyautogui.moveTo(x=-1228, y=743)
        pyautogui.click()
        pyautogui.moveTo(x=-1111, y=669)
        pyautogui.click()
        pyautogui.write("7")              #zniżka procentowa
        pyautogui.moveTo(x=-1181, y=741)
        pyautogui.click()
        # pyautogui.moveTo(x=-1246, y=715)
        # pyautogui.click()
        # pyautogui.moveTo(x=-1206, y=853)
        # pyautogui.click()
        # pyautogui.moveTo(x=-1235, y=790)
        # pyautogui.click()
        pyautogui.moveTo(x=-1048, y=886)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(x=-1046, y=750) #Wróć do listy
        pyautogui.click()
    except:
        break
#=====================================================================

#size 90% 1920x1080 Blackweek kategorii add
pyautogui.PAUSE = 1.5
pyautogui.moveTo(x=-1645, y=309)
pyautogui.click(clicks=2)
pyautogui.write("4564")
pyautogui.press("enter")
pyautogui.moveTo(x=-1409, y=522)
pyautogui.click()
pyautogui.moveTo(x=-1545, y=454)
pyautogui.click()
pyautogui.moveTo(x=-1182, y=492)
pyautogui.click()
pyautogui.moveTo(x=-701, y=1009)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(x=-1645, y=301)
pyautogui.click(clicks=2)
#=========================================================================





