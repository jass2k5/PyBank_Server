from utils.valid_input import (get_valid_amount,get_valid_name)
from src.accounts import Account
import random
import string
import json
class Banking_system:
    filename = "data/accounts.json"
    def __init__(self,filename,accountnumber,name,pin,balance = 0):
        self.data = Account(self,filename,accountnumber,name,pin,balance)
        self.acc_holder_data = []
    def save_data(self):
    def add_account(self):
        while True:
            #asking if user want to continue
            print("enter y/n to continue or  exit..\n")
            yesorno = input("Y/N").upper()
            if yesorno == "N":
                print("goodbye")
                break
            #generating account jsut like passwords
            character = string.ascii_letters + string.digits
            self.data.account_number = ""
            for i in range(1,10):
                #adding to the account object
                self.data.account_number += random.choice(character)
            print(f"ACCOUNT NUMBER = {self.data.account_number}")
            #asking for a name now 
            name = input("enter your name ")
            user_name = get_valid_name(name)
            if user_name is None:
                print("enter a valid name").title()
                continue
            self.data.name = user_name
            print(f"entered name:{self.data.name}")
            #making the 4 digit pincode
            pincode = string.digits
            for i in range(1,4):
                self.data.__pin += random.choice(pincode)
            print("Pin code generated request the servers to reveal the pincode\n")
            #adding money to account
            print("rule - account holder must deposit 500 rupees to start account")
            while True:
                try:
                    Balance = int(input("deposit the money"))
                    if Balance < 500:
                        print("enter atleast 500 rupees").title()
                        continue
                    break
                except(ValueError or TypeError):#will use gui in future to have digit only keyword to enter input
                    print("enter digit only")
                    continue
            print("request the servers to know what's your balance")
                   




    def add_amount(self):
        while self.chances > 0:
            print("you have 3 chances to enter pin correctly other wise your acc will be blocked\n").title()
            user_pin = input("enter a 4 digit pin:").strip()
            if not user_pin.isdigit() or len(user_pin) != 4:
                print("enter the pin in right format")
                self.chances -= 1
                continue
            if user_pin == self.data.__pin:
                amount = input("enter the amount")
                entered_amount = get_valid_amount(amount)
                if entered_amount is not None:
                    self.data.__balance += entered_amount
                    print(f"entered amount{entered_amount}\n".title())
                    print("updated balance ")
                    self.balance()
                    break
            else:
                self.chances -= 1
                continue
    