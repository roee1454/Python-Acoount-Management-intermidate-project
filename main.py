#Roee's Bank
import sys,random,rstr, typing
from tkinter import Tk, ttk
from tkinter import *

class Account:
    def __init(self, user_code, password):
        self.user_code = user_code
        self.password = password
    def register(self):
        pass
    def login(self):
        pass


class Bank_System:
    def __init__(self,account: Account):
        self.account = account
    def get_mastercard(self, half_num):
        mastercard_num = f"53573862{half_num}"
        return mastercard_num
    def deposit(self):
        pass
    def transfer(self):
        pass
    def get_paycheck(self):
        pass


class GUI:
    def __init__(self,root):
        self.root = root
        self.size = (640,480)
        self.root.title("Bank Prototype")
        self.icon = PhotoImage(file="assets\\icon.png")
        self.root.iconphoto(False,self.icon)
        self.root.geometry(f"{self.size[0]}x{self.size[1]}")
        self.root.resizable(False,False)
        self.login()
    def login(self):
        for widget in self.root.winfo_children():
            widget.place_forget()
        self.frame = Frame(self.root, width=self.size[0], height=self.size[1], background="white")
        self.frame.pack()
        frame_bg = self.frame["background"]
        self.big_title1 = ttk.Label(self.frame, text="Welcome to my bank!", foreground="red", background=frame_bg)
        self.big_title1.place(x=self.size[0]/2-60,y=10)
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
        self.login_button = ttk.Button(self.frame, width=30, text="Login")
        self.login_button.place(x=self.size[0]/2-100, y=250)
        self.register_label = ttk.Label(self.frame, text="Aren't having an account?", foreground="blue", background=frame_bg)
root = Tk()
gui = GUI(root)
root.mainloop()