import cmd
import glob
import keyboard
import os
import pythoncom
import win32com.client
import win32con
import win32process
import win32gui

def ShowWindow():
    # Need this for some reason otherwise SetForegroundWindow will fail sometimes
    pythoncom.CoInitialize()
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys("%")
    # ^^^^^^^^^^
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.BringWindowToTop(hwnd)
    win32gui.SetForegroundWindow(hwnd)

def HideWindow(keyEvent):
    if (win32gui.GetForegroundWindow() == hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

class Command():
    def __init__(self, filename):
        file = open(filename, 'r')
        self.lines = file.readlines()

    def Run(self):
        for line in self.lines:
            print(line)

class ThingerShell(cmd.Cmd):
    intro = "Welcome to the thinger shell. Type help or ? to list commands.\n"
    prompt = "> "

    def __init__(self):
        super(ThingerShell, self).__init__()
        self.LoadCommands()

    def do_quit(self, arg):
        "Exit Thinger"
        print("Bye!")
        return True

    def UserCmd(self, arg):
        self.commands[self.lastcmd].Run()
        print()

    def UserCmdHelp(self):
        # Todo: custom help text per command
        print()

    def LoadCommands(self):
        # Get list of all *.cmd files in /Commands directory
        cwdSave = os.getcwd()
        os.chdir(os.path.join(os.getcwd(), "Commands"))
        commandFilenames = glob.glob("*.cmd")

        # Create command objects + hooks for each *.cmd file
        self.commands = dict()
        for filename in commandFilenames:
            commandName = filename.split(".")[0]
            self.commands[commandName] = Command(filename)
            setattr(ThingerShell, "do_" + commandName, ThingerShell.UserCmd)
            setattr(ThingerShell, "help_" + commandName, ThingerShell.UserCmdHelp)

        # Reset working dir
        os.chdir(cwdSave)

if __name__ == '__main__':
    # Setup hotkeys + window management logic
    hwnd = win32gui.GetForegroundWindow()
    keyboard.add_hotkey("ctrl+shift+j", ShowWindow, suppress=True)
    keyboard.on_press_key("esc", HideWindow)

    # Start up prompt
    thinger = ThingerShell()
    thinger.cmdloop()