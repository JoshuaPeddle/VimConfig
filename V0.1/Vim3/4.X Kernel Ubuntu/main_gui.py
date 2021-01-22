from tkinter import *
from env_gui import toplevel
import subprocess

def onclick(i):
    print('This is Button: ' + str(i))
    return


def open_env_tools_gui():

    toplevel()

def start():
    # Win config
    win = Tk()
    win.tk_bisque()
    win.geometry('200x300')
    win.title('Vim Tools : Home page')
    # Frame 1
    frame1 = Frame(win, width=100, height=100, background='bisque')
    frame1.pack()
    # Top label
    var = StringVar()
    label = Label(frame1,font=("Arial", 20) , textvariable=var, relief=RAISED)
    var.set('VimTools v0.1')
    label.pack(side=TOP)

    # frame2 Left Label
    # CPU configuration, System monitor and env.txt tools are accessed here
    frame2 = Frame(win, width=100, height=100, background='bisque')
    frame2.pack(side=LEFT)
    # Button 1
    b = Button(frame2, height=1, width=15,text= 'CPU configuration', command=lambda i=0: onclick(i))
    b.pack()
    # Button 2
    b = Button(frame2, height=1, width=15, text='System monitor', command=lambda i=1: onclick(i))
    b.pack()
    # Button 2
    b = Button(frame2, height=1, width=15, text='env.txt tools', command=lambda i=1: open_env_tools_gui())
    b.pack()
    # Start
    win.mainloop()


start()
