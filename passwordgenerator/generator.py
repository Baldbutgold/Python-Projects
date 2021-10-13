import clipboard
import string
import random

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

password_length = input("How long do you want your password to be?\n")
#colored warning

choice = input("""Seperate Using Space
Press 1 for lowercase
Press 2 for uppercase
Press 3 for digits
Press 4 for symbols
Press 5 for everything\n""")

def listbuilder():
    global list
    list= ''
    if '1' in choice: 
        list += lower_case
    if '2' in choice:
        list += upper_case
    if '3' in choice:
        list += digits
    if '4' in choice:
        list += symbols
    if '5' in choice:
        list = lower_case + upper_case + digits + symbols

def passwordgenerator(list, password_length):
    global password
    password = ''
    try:
        for i in range(int(password_length)):
            index = random.randint(0, int(len(list)))
            password += list[index - 1]
    except:
        print('Something went wrong, check the length you have provided')

def passwordretriever():
    print('Here is your password : {}'.format(password))
    copy = input("Do you want to copy it to your clipboard y or n\n")
    if 'y' in copy:
        #copy to clipboard
        clipboard.copy(password)
    elif 'Y' in copy:
        clipboard.copy(password)
        #copy to clipboard
    else:
        quit()

listbuilder()
passwordgenerator(list, password_length)
passwordretriever()
