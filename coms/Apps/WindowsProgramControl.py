from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import warnings
import time
# https://github.com/pywinauto/pywinauto

import win32com.client as comclt
wsh= comclt.Dispatch("WScript.Shell")
  
# WindowsProgramControl.py
# this uses a very powerful library that can execute many windows api calls
# many different apps may take use from the functions in this file
# e.g the spotify app will call this library to open spotify if it is not open yet



app = None
windows = None

def setup():
    global app
    global windows
    app = Application()
    windows = Desktop(backend="uia").windows()
    warnings.simplefilter('ignore', category=UserWarning)  # turns off annoying 32-bit warnings

def openProgram(path):
    global app
    try:
        app = app.connect(path=path)
    except Exception as e:
        try:
            app = Application().start(path)
        except Exception as ex:
            print(ex)

# returns a list of open windows
def getOpenWindows():
    global windows
    openWindowsString = []
    for w in windows:
        if len(w.window_text()) > 0 and not (w.window_text() == "Taskbar" or w.window_text() == "Program Manager"):
            openWindowsString.append(w.window_text())
    # print(openWindowsString)
    # also get the icon images????
    return openWindowsString

# if the given program is open, switches the focus to it (bring to front)
# todo: add better way to do this without name (some sort of hash, best to store hash also on the RPi)
def switchFocus(name):
    try:
        app.connect(title_re=".*%s" % name, visible_only=True, found_index=0)
        app_dialog = app.window(title_re=".*%s.*" % name, visible_only=True, found_index=0)
        if app_dialog.exists():
            app_dialog.set_focus()
    except Exception as e:
        print(e)

# minimizes the given program by name
# todo: add better way to do this without name (some sort of hash, best to store hash also on the RPi)
def minimizeProgByName(name):
    try:
        app.connect(title_re=".*%s" % name, visible_only=True, found_index=0)
        app_dialog = app.window(title_re=".*%s.*" % name, visible_only=True, found_index=0)
        if app_dialog.exists():
            app_dialog.minimize()
            return
    except Exception as e:
        print(e)


# setup()
# switchFocus("Chrome")
# wsh.SendKeys(" ") # send the keys you want