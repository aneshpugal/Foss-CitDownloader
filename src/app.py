#!/usr/bin/#!/usr/bin/env python3

from tkinter import *
from time import sleep
import pysftp

#Process download
def procRequest():
    #Retrieve input values
    server = inp_server.get()
    uname = inp_uname.get()
    passw = inp_pass.get()
    proj = inp_proj.get()

    #Disable hostkeys
    lbl_status.configure(text='Establishing connection....')
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    #Create connection
    con = pysftp.Connection(server,username=uname,password=passw,cnopts=cnopts)
    lbl_status.configure(text='Connection Successfull')
    sleep(1)

    #Download project
    if(con.isdir(proj)):
        lbl_status.configure(text="Downloading Project '"+proj+"'...")
        con.get_r(proj,'downloads')
        lbl_status.configure(text='Downloading complete...')
    else:
        lbl_status.configure(text='PROJECT NOT FOUND IN SERVER')

#INIT
if __name__ == '__main__':
    window = Tk()

    #GLOBALS
    img = PhotoImage(file='assets/logo.png')

    #WINDOW PROPERTIES
    window.title('FOSS-CIT Project Downloader')
    window.geometry('600x600')
    window.resizable(False,False)
    window.wm_iconbitmap('assets/icon.ico')

    #LABELS
    logo = Label(image=img)
    lbl_server = Label(text='Server:')
    lbl_uname = Label(text='Username:')
    lbl_pass = Label(text='Password:')
    lbl_proj = Label(text='Project:')
    lbl_status = Label(text='Enter details and press button')

    #INPUTS
    inp_server = Entry()
    inp_uname = Entry()
    inp_pass = Entry()
    inp_proj = Entry()
    inp_submit = Button(text='Get Project',command=procRequest)

    #PACKING
    logo.pack()
    lbl_server.pack()
    inp_server.pack()
    lbl_uname.pack()
    inp_uname.pack()
    lbl_pass.pack()
    inp_pass.pack()
    lbl_proj.pack()
    inp_proj.pack()
    inp_submit.pack()
    lbl_status.pack()

    window.mainloop()
