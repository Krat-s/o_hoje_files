import pyautogui as pg
import time

print('hoj')

def trol():
    time.sleep(3)
    # pg.click(x=229, y=480)
    pg.click(x=246, y=101)
    time.sleep(.8)
    pg.click(x=366, y=946)
    pg.write('ahhhhhhhh')
    pg.press('enter')
    pg.hotkey('alt', '3')


trol()
          