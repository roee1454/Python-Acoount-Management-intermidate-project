import sys,random,rstr, typing, json
from tkinter import Tk, ttk, messagebox
from tkinter import *
from main import GUI


class login():
    def __init__(self, master):
        pass
    def login(self):
        for widget in master.winfo_children():
            widget.pack_forget()
        self.frame = Frame(master, width=self.size[0], height=self.size[1], background="white")
        self.frame.pack()
        frame_bg = self.frame["background"]
        self.big_title1 = ttk.Label(self.frame, text="Welcome to the Dollar bank!", foreground="red", background=frame_bg)
        self.big_title1.place(x=self.size[0]/2-75,y=10)
        self.big_title2 = ttk.Label(self.frame, text="Enter Usercode and Password to see your current state", foreground="red",background=frame_bg)
        self.big_title2.place(x=self.size[0]/2-140,y=40)
        self.user_code_label = ttk.Label(self.frame, text="User Code:", foreground="black",background=frame_bg)
        self.user_code_label.place(x=120,y=100)
        self.password_label = ttk.Label(self.frame, text="Password:", foreground="black",background=frame_bg)
        self.password_label.place(x=120, y=160)
        self.input1 = ttk.Entry(self.frame, width=35)
        self.input1.place(x=self.size[0]-300,y=100)
        self.input2 = ttk.Entry(self.frame, width=35)
        self.input2.place(x=self.size[0]-300,y=160)
        self.login_button = ttk.Button(self.frame, width=30, text="Login", command=self.login_account)
        self.login_button.place(x=self.size[0]/2-100, y=250)
        self.register_label = ttk.Label(self.frame, text="Aren't having an account yet?", foreground="blue", background=frame_bg)
        self.register_label.place(x=120,y=300)
        self.preregister_button = ttk.Button(self.frame, width=20, text="Register Here!", command=self.register)
        self.preregister_button.place(x=350,y=300)
    
