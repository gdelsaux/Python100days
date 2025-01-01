import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""

print("Welcome to the PyPassword generator!")

password_lenght = int(input("How many characters would you like in your password?\n"))

# Password's numbers
number_of_numbers = int(input("How many numbers would you like in your password?\n"))
if number_of_numbers > password_lenght:
    print("You choose more numbers than available characters for your password!")
    exit(1)
    
# Number of Symbols
number_of_symbols = int(input("How many symbols would you like in your password?\n"))
if number_of_numbers + number_of_symbols > password_lenght:
    print("The combined amount of numbers and symbols is greater than your password!")
    exit(1)

for character in range(0, password_lenght + 1):
    print(f"num: {number_of_numbers}, sym: {number_of_symbols}")
    if number_of_numbers > 0:
        print("num")
        number_of_numbers -= 1
        password += symbols[random.randint(0, len(symbols)) - 1]
    elif number_of_symbols > 0:
        print("sym")
        number_of_symbols -= 1
        password += numbers[random.randint(0, len(numbers)) - 1]
    else:
        print("Char")
        password += letters[random.randint(0, len(letters)) - 1]

def shuffle_password(string):
    # Turn the string into a list
    password_list = list(string)
    # Shuffle the list
    random.shuffle(password_list)
    # Return the joint list
    # note that the empty string is what the item will be joined with ex: '-'.join([1, 2, 3]) will be 1-2-3
    return ''.join(password_list)

print(f"Your password is: {shuffle_password(password)}")
