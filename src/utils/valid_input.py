def get_valid_amount(user_amount):
    try:
        user_amount = float(user_amount)
        if user_amount <= 0 :
            print("enter amount greater than 0")
            return None
        return user_amount
    except (TypeError,ValueError):
        return None
def get_valid_name(name):
    try:
        if not name.replace(" ","").isalpha():
            return None       
        return name 
    except(TypeError):
        return None
def get_valid_phone(phone):
        if len(phone) != 10 or not phone.isdigit():
            return None
        else:
            return int(phone)
    

    