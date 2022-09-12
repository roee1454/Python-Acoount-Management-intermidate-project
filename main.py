#Roee's Bank
import sys,random,rstr, typing, json
from tkinter import Tk, ttk, messagebox
from tkinter import *
from Authentication.account import Account


def has_digit(string: str):
    return any([char.isdigit() for char in string])
def toogle_entry(entry, var):
    if var.get() == 0:
        entry.config(state=DISABLED)
    if var.get() == 1:
        entry.config(state=NORMAL)

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
    def menu_bar(self, account_info, user_account: Account):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        main_menu = Menu(self.menu)
        self.menu.add_cascade(label="Main", menu=main_menu)
        main_menu.add_command(label="Balance Info", command=lambda: self.view_balance(account_info))
        main_menu.add_command(label="Edit Info", command=lambda: self.edit_info(account_info, user_account))
    def login(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.frame = Frame(self.root, width=self.size[0], height=self.size[1], background="white")
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
    def register(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.frame = Frame(self.root, width=self.size[0], height=self.size[1], background="white")
        self.frame.pack()
        frame_bg = self.frame["background"]
        self.big_title1 = ttk.Label(self.frame, text="Register to the Dollar bank!", foreground="red", background=frame_bg)
        self.big_title1.place(x=self.size[0]/2-75,y=10)
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
        self.login_label = ttk.Label(self.frame, text="Having an account already?", foreground="blue", background=frame_bg)
        self.login_label.place(x=120,y=380)
        self.prelogin_button = ttk.Button(self.frame, width=20, text="Login Here!", command=self.login)
        self.prelogin_button.place(x=350,y=380)
    def reg_account(self):
        if self.input1.get() != "" and self.input2.get() != "" and self.input3.get() != "" and self.input4.get() != "" and self.input5.get() != "":
            if has_digit(self.input3.get()) and len(self.input3.get()) >=4:
                if len(self.input4.get()) >= 8:
                    new_account = Account(user_code=self.input3.get(), password=self.input4.get())
                    new_account.register(first_name=self.input1.get(),last_name=self.input2.get(),phone_num=self.input5.get())
                    messagebox.showinfo(title="Register", message="Registered Successfully!")
                    self.login()
                else: messagebox.showerror(title="Register", message="Password length needs to be 8 characters or more!")
            else: messagebox.showerror(title="Register", message="Usercode length needs to be 4 characters or more!\nMoreover, most contain at least 1 digit!")
        else:
            messagebox.showerror(title="Register", message="Please fill all blank fields!")
    def login_account(self):
       # try:
            user_account = Account(self.input1.get(), self.input2.get())
            login = user_account.login()
            if login[0]: 
                messagebox.showinfo(title="Login", message="Logged In!") 
                self.main_screen(login[1], user_account)
            else: messagebox.showerror(title="Login", message="One or both of your creditionals are not valid!")
        #except:
            #messagebox.showerror(title="Login", message="One or both of your creditionals are not valid!")
    def save_edit_info(self,popup: Toplevel, entry1: Entry, entry2: Entry, account,user_account: Account):
        ans = messagebox.askyesno(title="Edit Info", message="Are you sure you want to save this changes?",parent=popup)
        if ans: 
            account = user_account.edit_info(entry1.get(), entry2.get())
            popup.destroy()
        else: pass
    def main_screen(self, account_info, user_account: Account):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        self.menu_bar(account_info, user_account)
        self.frame = Frame(self.root, width=self.size[0], height=self.size[1], background="white")
        self.frame.pack()
        frame_bg = self.frame["background"]
    def view_balance(self,account_info):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Balance Info")
        self.new_window.iconphoto(False,self.icon)
        self.new_window.geometry("200x100")
        self.new_window.resizable(False,False)
        frame = Frame(self.new_window, width=200, height=100, background="white")
        frame.pack()
        balance_label = ttk.Label(self.new_window ,text=f"Current Balance: {account_info['balance']}$", font=("Roboto", "10"), background=frame["background"])
        balance_label.place(x=frame["width"]/2-75,y=40)
    def edit_info(self, account_info, user_account: Account):
        self.new_window = Toplevel(self.root)
        self.new_window.attributes("-topmost",True)
        self.new_window.title("Edit Account Info")
        self.new_window.iconphoto(False,self.icon)
        self.new_window.geometry("400x300")
        self.new_window.resizable(False,False)
        frame = Frame(self.new_window, width=400, height=300, background="white")
        frame.pack()
        old_code_label = ttk.Label(self.new_window, text="Old User Code:", font=("Roboto", "10"), background=frame["background"])
        old_code_label.place(x=50,y=70)
        old_code_entry = ttk.Entry(self.new_window, width=20)
        old_code_entry.insert(0, account_info["user_code"])
        old_code_entry.place(x=150,y=70)
        old_code_entry.config(state=DISABLED)
        old_code_edit_label = ttk.Label(self.new_window, text="Edit", font=("Roboto", "10"), background=frame["background"])
        old_code_edit_label.place(x=300,y=70)
        old_code_var = IntVar()
        old_code_edit_checkbox = ttk.Checkbutton(self.new_window, variable=old_code_var,onvalue=1,offvalue=0,command=lambda: toogle_entry(old_code_entry, old_code_var))
        old_code_edit_checkbox.place(x=340,y=70)
        old_password_label = ttk.Label(self.new_window, text="Old Password:", font=("Roboto", "10"), background=frame["background"])
        old_password_label.place(x=50,y=140)
        old_password_entry = ttk.Entry(self.new_window, width=20)
        old_password_entry.insert(0, account_info["password"])
        old_password_entry.place(x=150,y=140)
        old_password_entry.config(state=DISABLED)
        old_password_edit_label = ttk.Label(self.new_window, text="Edit", font=("Roboto", "10"), background=frame["background"])
        old_password_edit_label.place(x=300,y=140)
        old_password_var = IntVar()
        old_password_edit_checkbox = ttk.Checkbutton(self.new_window, variable=old_password_var,onvalue=1,offvalue=0,command=lambda: toogle_entry(old_password_entry, old_password_var))
        old_password_edit_checkbox.place(x=340,y=140)
        save_button = ttk.Button(self.new_window, text="Save Changes", width=15, command=lambda: self.save_edit_info(self.new_window, old_code_entry, old_password_entry, account_info, user_account))
        save_button.place(x=150, y=200)

if __name__ == "__main__":
    App = Tk()
    gui = GUI(App)
    App.mainloop()