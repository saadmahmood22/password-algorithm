##
## ***************************************************
##   Saad Bhutta (20816830)
##   CS 116 Winter 2020
##   Assignment 03 Problem 04
## ***************************************************
##

def length_condition(password):
    '''
    Returns 1 if password has at least 10 characters, and 0 otherwise
    
    length_condition: Str -> Nat
    '''
    if len(password) >= 10:
        return 1
    else:
        return 0
    
def uppercase_condition(password):
    '''
    Returns 1 if password has at least 1 uppercase character, and 0 otherwise
    
    uppercase_condition: Str -> Nat
    '''
    if password == "":
        return 0
    elif password[0].isupper():
        return 1
    else:
        return uppercase_condition(password[1:])
    
def lowercase_condition(password):
    '''
    Returns 1 if password has at least 1 lowercase character, and 0 otherwise
    
    lowercase_condition: Str -> Nat
    '''
    if password == "":
        return 0
    elif password[0].islower():
        return 1
    else:
        return lowercase_condition(password[1:])
    
def non_alphanumeric_characters(password):
    '''
    Returns the number of non-alphanumeric characters in password
    
    non_alphanumeric_characters: Str -> Nat
    '''
    if password == "":
        return 0
    elif password[0].isalnum():
        return non_alphanumeric_characters(password[1:])
    else:
        return 1 + non_alphanumeric_characters(password[1:])
    
def non_alphanumeric_condition(password):
    '''
    Returns 1 if the number of non-alphanumeric characters in password is
    greater than or equal to 3, and 0 otherwise
    
    non_alphanumeric_condition: Str -> Nat
    '''
    if non_alphanumeric_characters(password) >= 3:
        return 1
    else:
        return 0
    
def number_of_digits(password):
    '''
    Returns the number of digits in password
    
    number_of_digits: Str -> Nat
    '''
    if password == "":
        return 0
    elif password[0].isdigit():
        return 1 + number_of_digits(password[1:])
    else:
        return number_of_digits(password[1:])
    
def digit_condition(password):
    '''
    Returns 1 if password has at least 1 digit, and 0 otherwise
    
    digit_condition: Str -> Nat
    '''
    if number_of_digits(password) >= 2:
        return 1
    else:
        return 0
    
def space_condition(password):
    '''
    Returns 1 if password has no spaces, and 0 otherwise
    
    space_condition: Str -> Nat
    '''
    if password == "":
        return 1
    elif password[0] == " ":
        return 0
    else:
        return space_condition(password[1:])
    
def new_password():
    '''
    Prompts the user to enter a string, then prints Good if the string has at
    least 10 characters, at least 1 uppercase character, at least 1 lowercase 
    character, at least 3 non-alphanumeric characters, at least 2 digits, and
    contains no spaces. If the string satisfies 4 or 5 out of the above 
    mentioned conditions, the function prints Fair. If the string satisfies 3
    conditions or less, the function prints Weak.
    
    Effects:
    Reads input from keyboard
    Prints to screen
    
    new_password: None -> None
    
    Examples:
    If the user enters "" when new_password() is called, Weak is printed
    If the user enters "GoOdpaSWORD!!!32", when new_password() is called, \
    Good is printed
    ''' 
    password = input("Enter password: ")
    if length_condition(password) + uppercase_condition(password) + \
       lowercase_condition(password) + non_alphanumeric_condition(password) + \
       digit_condition(password) + space_condition(password) == 6:
        print("Good")
    elif (length_condition(password) + uppercase_condition(password) + \
          lowercase_condition(password) + non_alphanumeric_condition(password) \
          + digit_condition(password) + space_condition(password) == 5) or \
         (length_condition(password) + uppercase_condition(password) + \
          lowercase_condition(password) + non_alphanumeric_condition(password) \
          + digit_condition(password) + space_condition(password) == 4):
        print("Fair")
    else:
        print("Weak")
        
new_password()