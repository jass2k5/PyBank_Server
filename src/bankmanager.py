from utils.valid_input import (get_valid_amount,get_valid_name)
from accounts import Account
from datetime import datetime
import random
import string
import json
import os
class Banking_system:
    def __init__(self,filename):
        self.filename = filename
        self.acc_holder_data = []
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

        # Load existing notes if file exists, else start empty
        if not os.path.exists(self.filename) or os.stat(self.filename).st_size == 0:
            with open(self.filename, "w") as f:
                json.dump([], f)  # initialize empty list

        try:
            with open(self.filename, "r") as f:
                self.acc_holder_data = json.load(f)
        except json.JSONDecodeError:
            self.acc_holder_data = []  # fallback if file is empty or corrupted

    def save_data(self):
        with open(self.filename,"w") as f:
            json.dump(self.acc_holder_data,f,indent =4)

    def add_account(self):
        while True:
            #asking if user want to continue
            print("enter y/n to continue or  exit..\n")
            yesorno = input("Y/N").upper()
            if yesorno == "N":
                print("goodbye")
                break
            #asking for name to continue
            name = input("enter your name ")
            user_name = get_valid_name(name)
            if user_name is None:
                print("enter a valid name".title())
                continue
            print(f"entered name:{name}")
            #generating account jsut like passwords
            character = string.ascii_letters + string.digits
            account_number = ""
            for i in range(1,10):
                #adding to the account object
                account_number += random.choice(character)
            print(f"ACCOUNT NUMBER = {account_number}")
            #making the 4 digit pincode
            userpin = ""
            pincode = string.digits
            for i in range(1,4):
                userpin += random.choice(pincode)
            print("Pin code generated request the servers to reveal the pincode\n")
            #adding money to account
            print("rule - account holder must deposit 500 rupees to start account")
            while True:
                try:
                    balance = int(input("deposit the money"))
                    if balance < 500:
                        print("enter atleast 500 rupees")
                        continue
                    break
                except(ValueError or TypeError):#will use gui in future to have digit only keyword to enter input
                    print("enter digit only")
                    continue
            print("request the servers to know what's your balance\n")
            timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")
            print(f"account created at:{timestamp}")
            edited = None
            
            self.data = Account(self.filename,account_number,name,pincode,balance)
            self.acc_holder_data.append({
                "Name": self.data.name,
                "Account number": self.data.account_number,
                "Pincode": self.data.get_pincode(),
                "Balance": self.data.get_balance(),
                "created at": timestamp,
                "edited at": edited
            })
            self.save_data()
            self.add_amount()

    def add_amount(self):
        
        while True:
            print("enter y/n to deposit money or n to exit..\n")
            yesorno = input("Y/N").upper()
            if yesorno == "N":
                print("goodbye")
                break
            if not self.acc_holder_data:
                print("no data yet".title())
                break
            #asking for acc number to add balance to that acc number
            accno = input("enter your account number here to continue\n")
            addamount = int(input("enter the amount you want to add in digits"))
            #checking if balance is greater than 0  and is in digit 
            addingamount = get_valid_amount(addamount)
            if addingamount is None:
                print("enter amount greater than 0 or in digits")
                continue
            for value in self.acc_holder_data:
                if value['Account number'] == accno:
                    value['Balance'] += addingamount
                    value['edited at'] = datetime.now().strftime("%y-%m-%d %H:%M:%S")
                    print(f"Account number: {accno} is updated with balance:{value['Balance']}")
                    break
                else:
                    print("account not found!")
                    continue


       
        
        
    

test = Banking_system("data/accounts.json")
test.add_account()