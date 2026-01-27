##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Password Strength Checker & Generator                                                                                        #
# File Name: password_generator.py                                                                                                           #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: pchstpch                                                                                                                  #
#                                                                                                                                            #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import string
import secrets

def generatePassphrase(length):
    pass
    
def generateString(length):
    characters = string.ascii_letters + string.digits # + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for i in range(int(length)))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def generatePassword(length, mode):
    if mode == 1:
        passphrase = generatePassphrase(length)
        return passphrase
    elif mode == 2:
        stringPass = generateString(length)
        return stringPass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #