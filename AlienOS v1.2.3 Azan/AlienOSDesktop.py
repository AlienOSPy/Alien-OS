# importing the important stuff
from tkinter import*
from tkinter.messagebox import*
from tkinter.filedialog import*
import pygame

#setting up the window
root = Tk()
root.title("Alien OS Azan")
root.geometry("1920x1080")
root.configure(background="lavender")

pygame.mixer.init()
pygame.mixer.music.load("Icons and Sounds\Start.mp3")
pygame.mixer.music.play(1)

bgImage = PhotoImage(file="Icons and Sounds\Desktop.png")
Label(root, image=bgImage).place(relwidth=1, relheight=1)


# Main Features such as shutdown

def shutdown():
     root.destroy()
     exec(open('root/Shutdown.py').read())

def restart():
     root.destroy()
     exec(open('AlienOSDesktop.py').read())


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Shutdown", command=shutdown)
filemenu.add_command(label="Restart", command=restart)
menubar.add_cascade(label="AlienOS", menu=filemenu)


root.config(menu=menubar)


# Terminal
def terminal():
     exec(open('root/Terminal.py').read())


  
m = Menu(root, tearoff = 0) 
m.add_command(label ="Terminal", command=terminal) 
m.add_command(label ="Database Tool") 
m.add_separator() 
m.add_command(label ="ALIEN OS AZAN") 
  
def do_popup(event): 
    try: 
        pygame.mixer.music.load("Icons and Sounds\Click.mp3")
        pygame.mixer.music.play(1)
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
root.bind("<Button-3>", do_popup) 


####################################################################################################################################

# programs

def notepad():
     exec(open('root/Notes.py').read())          

icon = PhotoImage(file=r"Icons and Sounds\Notes.png")

button4 = Button(root, image=icon, relief=RAISED, command=notepad, bg="lavender").place(x=670, y=900)

# Calculator

def calc():
     exec(open('root/calc.py').read())

icon2 = PhotoImage(file=r"Icons and Sounds\Calc.png")

button5 = Button(root, image=icon2, relief=RAISED, command=calc, bg="lavender").place(x=770, y=900)


# File Manager

def FileManager():
     askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*")])

icon3 = PhotoImage(file=r"Icons and Sounds\folder.png")

button6 = Button(root, image=icon3, relief=RAISED, command=FileManager, bg="lavender").place(x=870, y=900)

# Games

def Games():
     askopenfilename(defaultextension=".py", filetypes=[("All Files","*.*")])

icon4 = PhotoImage(file=r"Icons and Sounds\games.png")

button7 = Button(root, image=icon4, relief=RAISED, command=Games, bg="lavender").place(x=970, y=900)

# Paint

def Paint():
     exec(open('root/Paint.py').read())

icon5 = PhotoImage(file=r"Icons and Sounds\paint.png")

button8 = Button(root, image=icon5, relief=RAISED, command=Paint, bg="lavender").place(x=1070, y=900)

# Tunes

def Tunes():
     exec(open('root/Tunes.py').read())

icon6 = PhotoImage(file=r"Icons and Sounds\tunes.png")

button9 = Button(root, image=icon6, relief=RAISED, command=Tunes, bg="lavender").place(x=1170, y=900)

root.mainloop()