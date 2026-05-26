import pyautogui as pg
import keyboard as kb
import time

def sleep_computer():
    pg.hotkey('win', 'x')
    pg.press('a')
    time.sleep(2)
    kb.press('enter')
    time.sleep(3)
    kb.write("Start-Sleep -Seconds 1; Add-Type -Assembly System.Windows.Forms; [System.Windows.Forms.Application]::SetSuspendState('Suspend', $false, $false)")
    kb.press('enter')



def shutdown_computer():
    pg.hotkey('win', 'x')
    pg.press('a')
    time.sleep(2)
    kb.write("Stop-Computer")
    kb.press('enter')

if __name__ == "__main__":
    shutdown_computer()