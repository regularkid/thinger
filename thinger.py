import keyboard
import os
# import readline
import win32con
import win32process
import win32gui

def ShowWindow():
    print("Show")
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.BringWindowToTop(hwnd)
    win32gui.SetForegroundWindow(hwnd)

def HideWindow(keyEvent):
    if (win32gui.GetForegroundWindow() == hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

# Init
hwnd = win32gui.GetForegroundWindow()
keyboard.add_hotkey('ctrl+shift+j', ShowWindow, suppress=True)
keyboard.on_release_key('esc', HideWindow)

# Main loop
done = False
while (not done):
    userInput = input("> ")
    if (userInput == "q"):
        done = True