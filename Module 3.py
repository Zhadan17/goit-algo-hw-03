#Завдання 1 :

import datetime

def get_days_from_today(date) : 
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    today = datetime.date.today()

    delta = today - date

    return delta.days



#Завдання 2 :

import random

def get_numbers_ticket(min, max, quantity) : 
    numbers = []


    if quantity > (max - min + 1) or min <= 0 or max > 1000 or min >= max or quantity <= 0:

        return numbers

    lottery = random.sample(range(min, max + 1), quantity)

    return sorted(lottery)


#Завдання 3 :
import re

def normalize_phone(phone_number) : 

    pattern = r"[^\d+]"
    replacement = ""
    formatted_phone = re.sub(pattern, replacement, phone_number)

    if formatted_phone.startswith("+") and len(formatted_phone) == 13:
        return formatted_phone

    elif formatted_phone.startswith("0") and len(formatted_phone) == 10:
        return "+38" + formatted_phone
    
    elif formatted_phone.startswith("380") and len(formatted_phone) == 12:
            return "+" + formatted_phone

    else:
            raise ValueError("Invalid phone number format.")