#Roee's Bank
import sys,random,rstr, typing, json
from tkinter import Tk, ttk, messagebox
from tkinter import *

class Account:
    def __init__(self, user_code, password):
        self.user_code = user_code
        self.password = password
    def register(self, first_name, last_name,phone_num,filename="database/database.json"):
        account_info = {"first_name": first_name,"last_name": last_name,"user_code": self.user_code, "password": self.password, "phone_num": phone_num, "balance": f"{random.randint(100, 500)}"}
        with open(filename, "r+") as file:
            json_file = json.load(file)
            json_file["accounts"].append(account_info)
            file.seek(0)
            json.dump(json_file, file, indent=6)
    def login(self, filename="database/database.json"):
        with open(filename, "r+") as file:
            json_file = json.load(file)
            for idx,account in enumerate(json_file["accounts"]):
                if self.user_code == account["user_code"]  and self.password == account["password"]:
                    return True, account
                else: continue
            return False



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
        self.login_button = ttk.Button(self.frame, width=30, text="Login", command=self.login_account)
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
        self.first_name_label = ttk.Label(self.frame, text="First Name:", foreground="black", background=frame_bg)
        self.first_name_label.place(x=120,y=100)
        self.last_name_label = ttk.Label(self.frame, text="Last Name:", foreground="black", background=frame_bg)
        self.last_name_label.place(x=120,y=160)
        self.user_code_label = ttk.Label(self.frame, text="User Code:", foreground="black",background=frame_bg)
        self.user_code_label.place(x=120,y=220)
        self.password_label = ttk.Label(self.frame, text="Password:", foreground="black",background=frame_bg)
        self.password_label.place(x=120, y=280)
        self.phone_num_label = ttk.Label(self.frame, text="Phone Number:", foreground="black",background=frame_bg)
        self.phone_num_label.place(x=120, y=340)
        self.input1 = ttk.Entry(self.frame, width=35)
        self.input1.place(x=self.size[0]-300,y=100)
        self.input2 = ttk.Entry(self.frame, width=35)
        self.input2.place(x=self.size[0]-300,y=160)
        self.input3 = ttk.Entry(self.frame, width=35)
        self.input3.place(x=self.size[0]-300,y=220)
        self.input4 = ttk.Entry(self.frame, width=35)
        self.input4.place(x=self.size[0]-300,y=280)
        self.input5 = ttk.Entry(self.frame, width=35)
        self.input5.place(x=self.size[0]-300,y=340)
        self.register_button = ttk.Button(self.frame, width=30, text="Register", command=self.reg_account)
        self.register_button.place(x=self.size[0]/2-100, y=420)
        self.login_label = ttk.Label(self.frame, text="Aren't having an account yet?", foreground="blue", background=frame_bg)
        self.login_label.place(x=120,y=380)
        self.prelogin_button = ttk.Button(self.frame, width=20, text="Login Here!", command=self.login)
        self.prelogin_button.place(x=350,y=380)
    def main_screen(self, account):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.frame = Frame(self.root, width=self.size[0], height=self.size[1], background="white")
        self.frame.pack()
        frame_bg = self.frame["background"]
        self.greet_client_label = ttk.Label(self.frame, text=f"Hey {account['first_name']}!", foreground="red", background=frame_bg, font=("Arial", 20))
        self.greet_client_label.place(x=self.size[0]/2-70,y=25)
        self.balance_client_label = ttk.Label(self.frame, text=f"Balance: {account['balance']}$", foreground="black", background=frame_bg, font=("Arial", 20))
        self.balance_client_label .place(x=self.size[0]/2-80,y=85)
    def reg_account(self):
        if self.input1.get() != "" and self.input2.get() != "" and self.input3.get() != "" and self.input4.get() != "" and self.input5.get() != "":
            new_account = Account(user_code=self.input3.get(), password=self.input4.get())
            new_account.register(first_name=self.input1.get(),last_name=self.input2.get(),phone_num=self.input5.get())
            messagebox.showinfo(title="Register", message="Registered Successfully!")
            self.login()
        else:
            messagebox.showerror(title="Register", message="Please fill all blank fields!")
    def login_account(self):
        try:
            user_account = Account(self.input1.get(), self.input2.get())
            login = user_account.login()
            if login[0] is True: 
                messagebox.showinfo(title="Login", message="Logged In!") 
                self.main_screen(login[1])
            elif login[0] is False: messagebox.showerror(title="Login", message="One or both of your creditionals are not valid!")
        except TypeError:
            messagebox.showerror(title="Login", message="One or both of your creditionals are not valid!")
            
root = Tk()
gui = GUI(root)
root.mainloop()