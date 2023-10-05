import pyautogui as pg
import time

time.sleep(3)

#it will show the screen resolution 
#print(pg.size())

#it will print the current position of the screen
#print(pg.position( ))

#to move the mouse cursor (width,height,time)
#pg.moveTo(1780,0,2)

#to click
pg.click(1780,0,1,2,button="left")

#to scroll +ve for upward and -ve to downward
#pg.scroll(500)

#drag mouse position down function will click left button untill another button is clicked or mouseup is used
pg.mouseDown(200,400,button="left")
pg.moveTo(800,400,2)
pg.mouseUp()