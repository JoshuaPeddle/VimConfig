from tkinter import *
from env_parser import *


def onclick(i):
    print('This is Button: ' + str(i))
    return


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def display_env(frametarget):
    ENV = load_env_file()
    #print(ENV.data)
    clear_frame(frametarget)  # Clear off the right frame
    # Top Label
    var2 = StringVar()
    label2 = Label(frametarget, textvariable=var2, relief=RAISED)
    var2.set('env.txt config:')
    label2.pack(side=TOP)

    # Fan control
    # Header
    var = StringVar()
    label = Label(frametarget,height = 2, width = 14, textvariable=var, relief=RAISED)
    var.set('Fan control:')
    label.pack(side=TOP,ipadx=2, ipady=2)
    # Result from envParser
    var = StringVar()
    label = Label(frametarget, height=2, width=14, textvariable=var, relief=RAISED)
    var.set(ENV.data['fan'])
    label.pack(side=TOP, ipadx=2, ipady=2)
    # HDMI autodetect
    # Header
    var = StringVar()
    label = Label(frametarget,height = 2, width = 14, textvariable=var, relief=RAISED)
    var.set('HDMI autodetect:')
    label.pack(side=TOP,ipadx=2, ipady=2)
    # Result from envParser
    var = StringVar()
    label = Label(frametarget, height=2, width=14, textvariable=var, relief=RAISED)
    var.set(ENV.data['autodetect'])
    label.pack(side=TOP, ipadx=2, ipady=2)
    # HDMI resolution
    # Header
    var = StringVar()
    label = Label(frametarget,height = 2, width = 14, textvariable=var, relief=RAISED)
    var.set('HDMI resolution:')
    label.pack(side=TOP,ipadx=2, ipady=2)
    # Result from envParser
    var = StringVar()
    label = Label(frametarget, height=2, width=14, textvariable=var, relief=RAISED)
    var.set(ENV.data['resolution'])
    label.pack(side=TOP, ipadx=2, ipady=2)
    # Kernel args
    # Header
    var = StringVar()
    label = Label(frametarget,height = 2, width = 14, textvariable=var, relief=RAISED)
    var.set('Kernel args: ')
    label.pack(side=TOP,ipadx=2, ipady=2)
    # Result from envParser
    var = StringVar()
    label = Label(frametarget, height=2, width=14, textvariable=var, relief=RAISED)
    var.set(ENV.data['kernel_args'])
    label.pack(side=TOP, ipadx=2, ipady=2)
    # Little core freq
    # Header
    var = StringVar()
    label = Label(frametarget,height = 2, width = 14, textvariable=var, relief=RAISED)
    var.set('Little core freq:')
    label.pack(side=TOP,ipadx=2, ipady=2)
    # Result from envParser
    var = StringVar()
    label = Label(frametarget, height=2, width=14, textvariable=var, relief=RAISED)
    var.set(ENV.data['little_cores'])
    label.pack(side=TOP, ipadx=2, ipady=2)
    # Big core freq
    # Header
    var = StringVar()
    label = Label(frametarget,height = 2, width = 14, textvariable=var, relief=RAISED)
    var.set('Big core freq:')
    label.pack(side=TOP,ipadx=2, ipady=2)
    # Result from envParser
    var = StringVar()
    label = Label(frametarget, height=2, width=14, textvariable=var, relief=RAISED)
    var.set(ENV.data['big_cores'])
    label.pack(side=TOP, ipadx=2, ipady=2)


def toplevel():
    # Win config
    tl = Toplevel()
    tl.tk_bisque()
    tl.geometry('300x600')
    tl.title('Vim Tools : env.txt')
    frame1 = None
    frame2 = None
    frame3 = None

    # Frame 1
    frame1 = Frame(tl, width=100, height=100, background='bisque')
    frame1.pack()
    # Top label
    var = StringVar()
    label = Label(frame1,font=("Arial", 20), textvariable=var, relief=RAISED)
    var.set('env.txt tools')
    label.pack(side=TOP)

    # Frame2
    frame2 = Frame(tl, width=100, height=100, background='bisque')
    frame2.pack(side=LEFT)
    # Button 1
    b = Button(frame2, height=1, width=15,text= 'Load enx.txt config',
               command=lambda i=0: display_env(frame3))
    b.pack()
    # Button 2
    b = Button(frame2, height=1, width=15, text='Edit env.txt config', command=lambda i=1: onclick(i))
    b.pack(side=LEFT)
    frame3 = Frame(tl, width=100, height=100, background='bisque')
    frame3.pack(side=RIGHT)


    # Start
    #win.mainloop()


#start()
