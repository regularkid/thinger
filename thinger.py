import keyboard
import os
import win32con
import win32process
import win32gui

def ShowWindow():
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

def HideWindow(keyEvent):
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

# Init
hwnd = win32gui.GetForegroundWindow()
keyboard.add_hotkey('ctrl+shift+j', ShowWindow)
keyboard.on_release_key('esc', HideWindow)

# Main loop
done = False
while (not done):
    userInput = input("> ")
    if (userInput == "q"):
        done = True