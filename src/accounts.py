class Account:
    def __init__(self,filename,account_number,name,pincode,balance = 0):
        self.filename = filename
        self.account_number = account_number
        self.name = name
        self.__pincode = pincode
        self.__balance = balance
    def get_pincode(self):
        return self.__pincode
    def get_balance(self):
        return self.__balance
    def __str__(self):
        return f"name = {self.name}\n,account_number = {self.account_number}"