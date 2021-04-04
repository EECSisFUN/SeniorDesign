from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import warnings
import time
import keyboard
from pynput.keyboard import Key, Controller
from Apps import WindowsProgramControl



def pressSpacebar(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def pressESC(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

def pressLeftArrow(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller(Program)
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def pressRightArrow(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def pressUpArrow(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    keyboard.press(Key.up)
    keyboard.release(Key.up)

def pressDownArrow(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    keyboard.press(Key.down)
    keyboard.release(Key.down)

def Fullscreen(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "f" 
    keyboard.press(key)
    keyboard.release(key)

def pressNum1(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "1"
    keyboard.press(key)
    keyboard.release(key)

def pressNum2(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "2"
    keyboard.press(key)
    keyboard.release(key)

def pressNum3(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "3"
    keyboard.press(key)
    keyboard.release(key)

def pressNum4(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "4"
    keyboard.press(key)
    keyboard.release(key)

def pressNum5(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "5"
    keyboard.press(key)
    keyboard.release(key)

def pressNum6(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "6"
    keyboard.press(key)
    keyboard.release(key)

def pressNum7(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "7"
    keyboard.press(key)
    keyboard.release(key)

def pressNum8(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "8"
    keyboard.press(key)
    keyboard.release(key)

def pressNum9(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "9"
    keyboard.press(key)
    keyboard.release(key)

def pressNum0(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "0"
    keyboard.press(key)
    keyboard.release(key)

def openPlayer(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "p" 
    keyboard.press(key)
    keyboard.release(key)

def closePlayer(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    key =  "x" 
    keyboard.press(key)
    keyboard.release(key)

def skipToNextItem(Program):
    WindowsProgramControl.switchFocus(Program)
    keyboard = Controller()
    keyboard.press(Key.shift)
    keyboard.press(Key.right)
    keyboard.release(Key.shift)
    keyboard.release(Key.right)
    keyboard.press(Key.shift)
    keyboard.press("n")
    keyboard.release(Key.shift)
    keyboard.release("n")