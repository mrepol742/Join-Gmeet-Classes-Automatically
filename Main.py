from time import sleep
import pyautogui as auto
import schedule, webbrowser

# Gmeet Code
code = "kvy-qhny-kjb"

# Time of class 24hours
time = "19:12" 


def join():
    webbrowser.open_new_tab('https://meet.google.com/' + code)
    sleep(7)
    # for windows and linux
    auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')
    # for macOS
    #auto.hotkey('command', 'd')
    #auto.hotkey('command', 'e')
    auto.click(1034, 569)


schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)