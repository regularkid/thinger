import keyboard
import os
# import readline
import pythoncom
import win32com.client
import win32con
import win32process
import win32gui

def ShowWindow():
    pythoncom.CoInitialize()
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.BringWindowToTop(hwnd)
    win32gui.SetForegroundWindow(hwnd)

def HideWindow(keyEvent):
    if (win32gui.GetForegroundWindow() == hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

if __name__ == '__main__':
    # Init
    hwnd = win32gui.GetForegroundWindow()
    keyboard.add_hotkey('ctrl+shift+j', ShowWindow, suppress=True)
    keyboard.on_press_key('esc', HideWindow)

    # def complete(text,state):
    #     print("Hello")
    #     results = ["example",None]
    #     return results[state]

    # import readline
    # readline.parse_and_bind( 'tab: complete' )
    # readline.set_completer(complete)

    # Main loop
    done = False
    while (not done):
        userInput = input("> ")
        if (userInput == "q"):
            done = True