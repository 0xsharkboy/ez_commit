#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
import os, sys

options = [ "clean         : Clean part of code",
            "deploy        : Deploy a new project version",
            "documentation : Add / Update documentation",
            "feature       : New part of code that can perform a specific action",
            "fix           : Correct part of code or mistake",
            "init          : Initialise a new piece of your project",
            "library       : Edit library content",
            "patch         : Remove bug from the project",
            "performance   : Saves resources and time",
            "revert        : Recovers part of the project",
            "rework        : Overhaul a part of the project",
            "style         : Edit graphical content",
            "test          : Add / Update part of test"]

types = [   "🧽 CLEAN |",
            "🚀 DEPLOY |",
            "📃 DOCUMENTATION |",
            "✨ FEATURE |",
            "🔧 FIX |",
            "🎀 INIT |",
            "📚 LIBRARY |",
            "🩹 PATCH |",
            "🌡 PERFORMANCE |",
            "♻️ REVERT |",
            "🔸 REWORK |",
            "🧁 STYLE |",
            "🧪 TEST |"]

def main():
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == ("-a" or "--all"):
            os.system("git add .")
        if sys.argv[i] == ("-p" or "--push"):
            push = True
    menu_entry_index = TerminalMenu(options, title="Commit type", menu_highlight_style=("fg_yellow",)).show()
    try:
        message = input("Enter your commit message: ")
    except KeyboardInterrupt:
        exit(0)
    os.system(f"git commit -m \"{types[menu_entry_index]} {message}\"")
    if push:
        os.system("git push")
if __name__ == "__main__":
    main()
