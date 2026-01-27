##############################################################################################################################################
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#                      /$$                   /$$                         /$$        |                                                        #
#                     | $$                  | $$                        | $$        | Author: Muneeb Mennad                                  #
#   /$$$$$$   /$$$$$$$| $$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$$| $$$$$$$   | Project Name: Password Strength Checker & Generator    #
#  /$$__  $$ /$$_____/| $$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$_____/| $$__  $$  | File Name: password_generator.py                       #
# | $$  \ $$| $$      | $$  \ $$|  $$$$$$   | $$    | $$  \ $$| $$      | $$  \ $$  | Project Start: 2026-01-24                              #
# | $$  | $$| $$      | $$  | $$ \____  $$  | $$ /$$| $$  | $$| $$      | $$  | $$  | Github Username: pchstpch                              #
# | $$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/| $$$$$$$/|  $$$$$$$| $$  | $$  |                                                        #
# | $$____/  \_______/|__/  |__/|_______/    \___/  | $$____/  \_______/|__/  |__/  |                                                        #
# | $$                                              | $$                            |                                                        #
# | $$                                              | $$                            |                                                        #
# |__/                                              |__/                            |                                                        #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).parent
file_path = BASE_DIR / 'words_alpha.txt'

def generatePassphrase(numWords):
    with open(file_path) as f:
        words = [word.strip() for word in f]
        password = ' '.join(secrets.choice(words) for i in range(numWords))
    return password
    
def generateString(length):
    characters = string.ascii_letters + string.digits # + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for i in range(int(length)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def generatePassword(mode):
    if mode == 1:
        print("How many words would you like your passphrase to be? (Enter a number from 4-8 inclusive)")
        numWords = int(input("Answer: "))
        while (numWords < 4) | (numWords > 8):
            print("Please enter a number between 4 and 8 (inclusive) to continue!")
            print()
            numWords = int(input("Answer: "))
        passphrase = generatePassphrase(numWords) 
        return passphrase
    
    elif mode == 2:
        print("How many characters would you like your password to be? (Enter a number from 8-32 inclusive)") 
        length = int(input("Answer: "))
        while (length < 8) | (length > 32):
            print("Please enter a number between 8 and 32 (inclusive) to continue!")
            print()
            length = int(input("Answer: "))
        stringPass = generateString(length)
        return stringPass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #