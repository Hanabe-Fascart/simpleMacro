//base imports to be used when creating the Macros module
from pyautogui import *
import pyautogui          // To locate pixels in the screen
import time               // To be able to give delay between actions
import keyboard           // To be able to Use the keyboard actions
import random             // To give random values, give a more human apearance for certain actions that requiere
import win32api, win32con // To be able to use the Mouse events, a windows API, faster than the Pythion API
// Could use pyautogui to click, but as said, Windows API is WAY faster

//Defines a "procedure" or a "function" to be called, receiving X and Y
def click(x,y):
    win32api.SetCursorPos((x,y))                            //set the cursor at X, Y coordinates
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) // defines a event to happen, pressing the left button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   // defines a event to happen, un pressing the left button