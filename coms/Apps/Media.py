from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import warnings
import time
import keyboard
from pynput.keyboard import Key, Controller

app = None

def switchFocus(name):
    try:
        app.connect(title_re=".*%s" % name, visible_only=True, found_index=0)
        app_dialog = app.window(title_re=".*%s.*" % name, visible_only=True, found_index=0)
        if app_dialog.exists():
            app_dialog.set_focus()
    except Exception as e:
        print(e)

def pressSpacebar():
    keyboard = Controller()
    key =  keyboard.Key.space
    keyboard.press(key)
    keyboard.release(key)

def pressESC():
    keyboard = Controller()
    key = keyboard.Key.esc
    keyboard.press(key)
    keyboard.release(key)

def pressLeftArrow():
    keyboard = Controller()
    key =  keyboard.Key.left
    keyboard.press(key)
    keyboard.release(key)

def pressRightArrow():
    keyboard = Controller()
    key =  keyboard.Key.right
    keyboard.press(key)
    keyboard.release(key)

def pressUpArrow():
    keyboard = Controller()
    key =  keyboard.Key.up
    keyboard.press(key)
    keyboard.release(key)

def pressDownArrow():
    keyboard = Controller()
    key =  keyboard.Key.down
    keyboard.press(key)
    keyboard.release(key)

def pressF():
    keyboard = Controller()
    key =  "f"
    keyboard.press(key)
    keyboard.release(key)

def pressNum1():
    keyboard = Controller()
    key =  "1"
    keyboard.press(key)
    keyboard.release(key)

def pressNum2():
    keyboard = Controller()
    key =  "2"
    keyboard.press(key)
    keyboard.release(key)

def pressNum3():
    keyboard = Controller()
    key =  "3"
    keyboard.press(key)
    keyboard.release(key)

def pressNum4():
    keyboard = Controller()
    key =  "4"
    keyboard.press(key)
    keyboard.release(key)

def pressNum5():
    keyboard = Controller()
    key =  "5"
    keyboard.press(key)
    keyboard.release(key)

def pressNum6():
    keyboard = Controller()
    key =  "6"
    keyboard.press(key)
    keyboard.release(key)

def pressNum7():
    keyboard = Controller()
    key =  "7"
    keyboard.press(key)
    keyboard.release(key)

def pressNum8():
    keyboard = Controller()
    key =  "8"
    keyboard.press(key)
    keyboard.release(key)

def pressNum9():
    keyboard = Controller()
    key =  "9"
    keyboard.press(key)
    keyboard.release(key)

def pressNum0():
    keyboard = Controller()
    key =  "0"
    keyboard.press(key)
    keyboard.release(key)