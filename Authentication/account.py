import sys,random,rstr, typing, json
from tkinter import Tk, ttk, messagebox
from tkinter import *

class Account:
    def __init__(self, user_code, password):
        self.user_code = user_code
        self.password = password
    def register(self, first_name, last_name,phone_num,filename="database/database.json"):
        account_info = {"first_name": first_name,"last_name": last_name,"user_code": self.user_code, "password": self.password, "phone_num": phone_num, "balance": f"{random.randint(100, 500)}", "cvv": f"{random.randint(100, 999)}"}
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
    def edit_info(self, new_usercode: str, new_password: str, filename="database/database.json"):
        print("worked")
        with open(filename, "r+") as file:
            json_file = json.load(file)
            for idx,account in enumerate(json_file["accounts"]):
                if self.user_code == account["user_code"]  and self.password == account["password"]:
                    account["user_code"] = new_usercode
                    account["password"] = new_password
                    return account
                else: pass
            file.seek(0)
            json.dump(json_file, file, indent=6)
    def get_creditcard(self):
        pass
    def transfer(self):
        pass
    def deposit(self):
        pass