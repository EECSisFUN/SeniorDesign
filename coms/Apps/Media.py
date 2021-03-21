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
    key = "spacebar"
    keyboard.press(key)
    keyboard.release(key)

