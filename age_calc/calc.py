'''
Ask user current year
Ask user birth year
Ouput age
'''

def calculator():
    print("Welcome to the age calc")
    current_year = ask_user_for_int("Input the current year: ")
    try:
        birth_year = ask_user_for_int_below_value("What year were you born? ", current_year)
    except ValueError:
        print("You're a time traveler!")
        return
    age = current_year - birth_year
    print(f"Your age is {age}")

def ask_user_for_int(prompt):
    valid_data = False
    while not valid_data: #valid_data != True
        str_data = input(prompt)
        try:
            user_int = int(str_data)
            valid_data = True
        except ValueError:
            print("Input must be int")

    return user_int

def ask_user_for_int_below_value(prompt, value):
    user_int = ask_user_for_int(prompt)
    if user_int > value:
        raise ValueError(f"Expected input to be less than {value}, was actually {user_int}")
    return user_int

def checks_below_value(data, value):
    if data < value:
        return data
    raise ValueError(f"Expected input to be less than {value}, was actually {data}")