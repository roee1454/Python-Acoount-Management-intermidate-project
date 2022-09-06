#Roee's Bank
import sys,random,rstr, typing, json
from tkinter import Tk, ttk
from tkinter import *

class Account:
    def __init__(self, user_code, password, phone_num):
        self.user_code = user_code
        self.password = password
        self.phone_num = phone_num
    def register(self):
        account_info = {f"{self.user_code}": [self.password]}
        file = open("database/database.json")
        json.dump(account_info, file)
        file.close()
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
            widget.pack_forget()
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
        self.register_label = ttk.Label(self.frame, text="Aren't having an account yet?", foreground="blue", background=frame_bg)
        self.register_label.place(x=120,y=300)
        self.preregister_button = ttk.Button(self.frame, width=20, text="Register Here!", command=self.register)
        self.preregister_button.place(x=350,y=300)
    def register(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.frame = Frame(self.root, width=self.size[0], height=self.size[1], background="white")
        self.frame.pack()
        frame_bg = self.frame["background"]
        self.big_title1 = ttk.Label(self.frame, text="Register to my bank!", foreground="red", background=frame_bg)
        self.big_title1.place(x=self.size[0]/2-60,y=10)
        self.big_title2 = ttk.Label(self.frame, text="Enter your account info here", foreground="red",background=frame_bg)
        self.big_title2.place(x=self.size[0]/2-80,y=40)
        self.user_code_label = ttk.Label(self.frame, text="User Code:", foreground="black",background=frame_bg)
        self.user_code_label.place(x=120,y=100)
        self.password_label = ttk.Label(self.frame, text="Password:", foreground="black",background=frame_bg)
        self.password_label.place(x=120, y=160)
        self.phone_num_label = ttk.Label(self.frame, text="Phone Number:", foreground="black",background=frame_bg)
        self.phone_num_label.place(x=120, y=220)
        self.input1 = ttk.Entry(self.frame, width=35)
        self.input1.place(x=self.size[0]-300,y=100)
        self.input2 = ttk.Entry(self.frame, width=35)
        self.input2.place(x=self.size[0]-300,y=160)
        self.input3 = ttk.Entry(self.frame, width=35)
        self.input3.place(x=self.size[0]-300,y=220)
        self.register_button = ttk.Button(self.frame, width=30, text="Register", command=self.reg_account)
        self.register_button.place(x=self.size[0]/2-100, y=300)
        self.login_label = ttk.Label(self.frame, text="Aren't having an account yet?", foreground="blue", background=frame_bg)
        self.login_label.place(x=120,y=350)
        self.prelogin_button = ttk.Button(self.frame, width=20, text="Login Here!", command=self.login)
        self.prelogin_button.place(x=350,y=350)
    def reg_account(self):
        reg_info = (self.input1.get(),self.input2.get(),self.input3.get())
        new_account = Account(reg_info[0],reg_info[1].reg_info[2])
        new_account.register()

root = Tk()
gui = GUI(root)
root.mainloop()