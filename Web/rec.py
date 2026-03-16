import pyautogui as pg
import time

current_hour = (time.localtime().tm_hour)
current_minute = (time.localtime().tm_min)

current_time_day = f"{current_hour:02d}:{current_minute:02d}"


def shootdown():
    for _ in range(15):
        pg.hotkey('alt', 'f4', presses=2)
        print(f"Current time: {current_time_day}")
        pg.hotkey('alt', 'f4')


def record_something(for_minutes):
    print(f"Current time: {current_time_day}")

    pg.hotkey('alt', 'f9')
    time.sleep(for_minutes * 60)
    pg.hotkey('alt', 'f9')



record_something(1)