# Importing the imporant stuff

from tkinter import*
from time import sleep
import pygame

root = Tk()
root.title("AlienOS 1.2.3")
root.geometry("1920x1080")
root.configure(background="lavender")

pygame.mixer.init()
pygame.mixer.music.load("Icons and Sounds\shutdown.ogg")
pygame.mixer.music.play(1)

bgImage1 = PhotoImage(file="Icons and Sounds\shutdown.png")
Label(root, image=bgImage1).place(relwidth=1, relheight=1)



label2 = Label(root, text="Shutting Down", font="Helvetica 48 bold").pack()


def shutdown():
     root.destroy()         

icon = PhotoImage(file=r"Icons and Sounds\Power.png")

button = Button(root, image=icon, relief=RAISED, command=shutdown, bg="lavender").place(x=900, y=700)

root.mainloop()