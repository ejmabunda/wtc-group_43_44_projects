# NB: NO SHOTCUTS PLEASE!

# Function 1: hexidecimal_to_decimal(hexNum)
def hexidecimal_to_decimal(hexNum:str)-> int:
    """
    This function takes a hexadecimal number as a string (hexNum) and converts it to its decimal equivalent.
    
    Convert this number to its base-10 (decimal) equivalent.
    
    Steps to solve:
    1. Write a loop to convert the number.
    2. Return the decimal representation of the hexadecimal number as an integer.
    
    So:
    hexidecimal_to_decimal('1A') should return 26.
    """
    letters = {
        "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
    }

    decimal = 0 # will store the final answer

    hexNum = hexNum.upper()

    exp = len(hexNum) - 1 # keeps track of the exponent
    for i in range(len(hexNum)):
        if hexNum[i] in letters.keys(): # character is a letter
            decimal += letters[hexNum[i]] * (16 ** exp)
        else: # character is a number
            decimal += int(hexNum[i]) * (16 ** exp)
        exp -= 1

    return decimal

# Function 4: validate_username(username)
def validate_username(username:str) -> str:
    """
    This function checks if a username is valid or not based on the following rules:
    
    1. The username can only contain letters (a-z, A-Z) and numbers (0-9). If the username has any special 
       characters (e.g., @, $, %, etc.), the function should return 'invalid username' and ask the user to try again..
    2. The username must start with a letter. It cannot begin with a number or any other symbol.

    Steps to solve:
    1. First, check if the first character of the username is a letter.
    2. Then, check if all characters in the username are letters or numbers.
    3. If either condition fails, return 'invalid username'. Otherwise, return 'valid username'.
    
    so:
    validate_username('John123') should return 'valid username'.
    validate_username('123John') should return 'invalid username'.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    if username[0].lower() in alphabet or :
        return 'invalid username'
    
    for letter in username:
        if letter.lower() not in alphabet and letter.lower() not in numbers:
            return 'invalid username'
    return 'valid username'
    

# Function 6: fruit_basket_guessing_game(guess: list, secret: list)
def fruit_basket_guessing_game(guess: list, secret: list) -> tuple:
    """
    This function compares two lists of fruits: guess and secret.
    
    - The guess list contains the fruits the player guessed.
    - The secret list contains the correct sequence of fruits.
    
    The function should compare these lists and return a tuple of two values:
    1. The number of fruits that are correct and in the correct position.
    2. The number of fruits that are correct but in the wrong position.
    
    Steps to solve:
    1. Loop through both lists and compare each fruit at the same index to count correct matches.
    2. Then check for correct fruits in the wrong position.
    
    Example:
    fruit_basket_guessing_game(['apple', 'banana', 'orange', 'grape'], ['apple', 'orange', 'banana', 'pear']) 
    should return (1, 2) because 'apple' is correct in the right position, and 'banana' and 'orange' are correct but in the wrong position.
    """
    correct = 0
    correctish = 0

    for fruit in guess:
        # Correct position and value
        if fruit in secret and guess.index(fruit) == secret.index(fruit):
            correct += 1
        # Correct value but not position
        elif fruit in secret and guess.index(fruit) != secret.index(fruit):
            correctish += 1

    return (correct, correctish)
        

# Function 8: convert_seconds_to_time(seconds)
def convert_seconds_to_time(seconds):
    """
    This function converts a number of seconds into a more readable format: hours, minutes, and seconds.
    
    Steps to solve:
    1. Convert the given number of seconds into hours by dividing by 3600.
    2. Convert the remaining seconds into minutes by dividing by 60.
    3. The remaining seconds will be what's left after subtracting the hours and minutes.
    
    Return a tuple of the form (hours, minutes, seconds)
    
    Example:
    convert_seconds_to_time(3661) should return (1, 1, 1) because 3661 seconds is 1 hour, 1 minute, and 1 second.
    """
    hours = round(seconds/3600)
    minutes = ((seconds/60) - hours) / 60
    seconds_ = seconds % 60

    return (hours, round(minutes), seconds_)

def main():
    # Just testing....
    print(hexidecimal_to_decimal("2A"))
    print(validate_username("123"))
    print(fruit_basket_guessing_game(['plum', 'banana', 'orange', 'grape'], ['apple', 'orange', 'banana', 'pear']))
    print(convert_seconds_to_time(190))

main()
