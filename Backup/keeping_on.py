import time
import pyautogui as pg

pg.FAILSAFE = True

def manter_pc_ligado():
    while True:
        print('...')
        pg.moveRel(50, 0)
        time.sleep(5)  
        pg.moveRel(-50, 0)  
        time.sleep(2) 
        print(  'PC mantido ligado com sucesso.')
    
manter_pc_ligado()

