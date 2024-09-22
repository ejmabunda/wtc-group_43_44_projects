# group_exercise.py
# Welcome to the Petrol Station App Challenge!

# TODO: Import any necessary modules
import re

# TODO: Implement user authentication function
def user_authentication(name: str, phone_number: str) -> bool:
    """
    This function should authenticate the user by asking for their name and phone number.
    It returns True if the user information is valid, otherwise False.
    """
    search_name = re.search("[a-zA-Z]*( [a-zA-Z]*)", name)
    search_phone_numer = re.search("\d{3} ?\d{3} ?\d{4}", phone_number)

    return search_name != None and search_phone_numer != None

# TODO: Implement the menu function
def menu():
    """
    This function displays the menu of items and options for the user.
    It should return a formatted menu string.
    """
    menu = 'Menu:'

    items = ['Snacks', 'Perishables', 'Diesel Price', 'Unleaded Price', 'Calculate Petrol', 'Exit']
    for i, item in enumerate(items):
        menu += f'\n{i + 1}. {item}'

    return menu

# TODO: Implement the petrol calculation function
def calculate_petrol(budget, petrol_type, price):
    """
    This function calculates how many liters of petrol the user can get for a given price.
    It should return a message with the calculated amount.
    """
    if budget <= 0:
        return 'Invalid price. Please enter a valid amount.'
    elif petrol_type not in ['unleaded', 'diesel']:
        return 'Invalid petrol type.'
    
    litres = budget/price
    return f'You can get {round(litres, 2)} liters of unleaded petrol.'

def is_valid(choice: str) -> bool:
    """Checks whether or not the user entered valid input
    
    Args:
        choice(str): The user's input
        
    Returns:
        True: If input is valid
        False: If input is invalid
    """
    try:
        choice = int(choice)
        if choice >= 1 and choice <= 6:
            return True
        raise Exception
    except Exception:
        return False

# TODO: Implement the main application function
def main(name, phone_number, choice):
    """
    This function should control the flow of the application.
    It should display the menu, process user choices, and provide responses.
    """
    if not user_authentication(name, phone_number):
        if len(phone_number) != 10:
            return 'Invalid phone number. Please enter a 10-digit number.'
        if name == "":
            return 'Invalid name. Please enter a valid name.'

    match choice[0]:
        case '1':
            print('That will be R16.99, thank you!')
        case '2':
            print('That will be R16.99, thank you!')
        case '3':
            print('That will be R16.99, thank you!')
        case '4':
            print('That will be R16.99, thank you!')
        case '5':
            choice = choice.split()
            return calculate_petrol(int(choice[-1]), choice[1], 1.2)
        case '6':
            return f'Goodbye, {name}!'
        case _:
            return 'Invalid choice. Please select a valid option.'

    return f'Goodbye, {name}!'

if __name__ == "__main__":
    # TODO: Add code to greet the user and call the main function
    name = input('Your name is? ')
    phone_number = input('Phone number? ')

    print(menu())
    choice = input('Choose an option from the menu: ')
    print(main(name, phone_number, choice))
