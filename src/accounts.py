import hashlib
class Account:
    def __init__(self,filename,account_number,name,userpin,balance,phonenumber):
        self.filename = filename
        self.account_number = account_number
        self.name = name
        self.__pincode = userpin
        self.__balance = balance
        self.phonenumber = phonenumber
    def get_pincode(self):
        return self.__pincode
    def get_balance(self):
        return self.__balance
    def hash_pin(self,userpin):
        return hashlib.sha256(userpin.encode()).hexdigest()
        
    def __str__(self):
        return f"name = {self.name}\n,account_number = {self.account_number}"