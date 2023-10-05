#need to open paint in the background to play this program
import pyautogui as pg
import time

time.sleep(2)
distance = 300

pg.click(1790,0,2,button="left")
pg.moveTo(200,400,2)

while distance>0:  
    pg.dragRel(distance,0,2, button="left")
    distance -= 20
    pg.dragRel(0,distance,2, button="left")
    pg.dragRel(-distance,0,2, button="left")
    distance -= 20
    pg.dragRel(0,-distance,2,button="left")
time.sleep(2)