import pyautogui as pg
import time

current_hour = (time.localtime().tm_hour)
current_minute = (time.localtime().tm_min)

current_time_day = f"{current_hour:02d}:{current_minute:02d}"

pg.PAUSE = 0.3 
pg.FAILSAFE = True

def shootdown():
    for _ in range(5):
        pg.click()
        pg.hotkey('alt', 'f4', presses=2)
        print(f"Current time: {current_time_day}")
        pg.press('enter')
        pg.hotkey('alt', 'tab')


def record_something(for_minutes):
    print(f"Current time: {current_time_day}")

    pg.hotkey('alt', 'f9')
    time.sleep(for_minutes * 60)
    pg.hotkey('alt', 'f9')

    print(f"Current time: {current_time_day}")

    pg.click(500, 500)
    shootdown()


horas = 2 * 60

record_something(0 * 60 + 1)