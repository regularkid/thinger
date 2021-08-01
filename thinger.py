import cmd
import keyboard
import os
import pythoncom
import win32com.client
import win32con
import win32process
import win32gui

def ShowWindow():
    pythoncom.CoInitialize()
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys("%")
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.BringWindowToTop(hwnd)
    win32gui.SetForegroundWindow(hwnd)

def HideWindow(keyEvent):
    if (win32gui.GetForegroundWindow() == hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

class ThingerShell(cmd.Cmd):
    intro = "Welcome to the thinger shell.   Type help or ? to list commands.\n"
    prompt = "> "

    # ----- basic Thinger commands -----
    def do_forward(self, arg):
        "Move the Thinger forward by the specified distance:  FORWARD 10"
        print("forward called")
    def do_right(self, arg):
        "Turn Thinger right by given number of degrees:  RIGHT 20"
        print("right called")
    def do_bye(self, arg):
        "Stop recording, close the Thinger window, and exit:  BYE"
        print("Thank you for using Thinger")
        return True

if __name__ == '__main__':
    # Init
    hwnd = win32gui.GetForegroundWindow()
    keyboard.add_hotkey("ctrl+shift+j", ShowWindow, suppress=True)
    keyboard.on_press_key("esc", HideWindow)

    ThingerShell().cmdloop()