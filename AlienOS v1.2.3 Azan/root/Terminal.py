# Terminal

import os

while True:
    UsrInput = input("AlienOS/root $ ")
    if UsrInput == "cd":
        print("AlienOS/root")
    elif UsrInput == "os_version":
        print("AlienOS Azan v1.2.3")
    elif UsrInput == "ls":
        print("+--------------------+")
        print("| calc.py, Notes.py, |")
        print("| paint.py, Tunes.py |")
        print("| Shutdown.py,       |")
        print("| Terminal.py        |")
        print("+--------------------+")
        print(".")
    elif UsrInput == "clear":
        os.system("cls")
    elif UsrInput == "exit":
        break
    exit()
    else:
        print("Invalid Command")