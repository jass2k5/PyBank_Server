from decimal import Decimal, InvalidOperation
import hashlib
import random
import string
# ------------------------------
# PIN / hash functions
#------------------------------
def Generate_account_number(length: int = 10) -> str:
    digits = "".join(random.sample(string.digits,k=6))
    letters = "".join(random.sample(string.ascii_letters,k=4)) #sample instead if choices to insure no repeatation of any digit or letter.
    account_number = "".join(random.sample(letters+digits,k =10))
    return account_number
def Generate_pin(length: int = 4) -> str:
    """ 
    generate a random numeric pin of lenght 4
    like the banks atm pin code system of india
    
    """
    return "".join(random.choices(string.digits, k =length))
def hash_pin(pin:str) -> str:
    """
    converting the 4 digit pin into teh SHA256 hash fro secure storage 
    input will be string so does the output and we will store the hash vr.of
    pin in json(current) or sql lite(future) for user security"""
    return hashlib.sha256(pin.encode()).hexdigest()
# ----------------------------------------
# VALID HELPERS
# ----------------------------------------

def valid_amount(amount) -> Decimal | None:
    #it will either return the Decimal or None by Decimal we mean the amount if its float.
    #we used Decimal for human level math precision in coding becuase float can cause amount problems while adding.
    try:
        amount = Decimal(str(amount)) 
        if amount >= 500:
            return amount
        return None
    except (InvalidOperation, ValueError): #valueerro for None,func etc and Inavlaid for Decimal errors like abc etc
        return None
    
def valid_name(name:str) -> str:
    return name if name.replace(" ","").isalpha() else None

def valid_phone(phone:str) -> str | None:
    return phone if phone.isdigit() and len(phone) == 10 else None #we took input as str for phone because we need to check length.

def valid_pin(pin) -> str | None:
    if pin.isdigit() and len(pin) == 4:
        return pin
    return None
def print_acc():
    account_number= Generate_account_number()
    print(account_number)
def print_pin():
    pin = Generate_pin()
    print(pin)
def print_hash(pin):
    hash = hash_pin(pin)
    print(hash)

