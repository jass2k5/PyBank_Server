class Account:
    def __init__(self,filename,accountnumber,name,pin,balance = 0):
        self.filename = filename
        self.account_number = accountnumber
        self.name = name
        self.__pin = pin
        self.__balance = balance
        self.chances = 3
        self.acc_holder_data = []
    def __str__(self):
        return f"name = {self.name}\n,account_number = {self.account_number}"