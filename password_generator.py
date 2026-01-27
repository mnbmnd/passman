########################################################
# Author: Muneeb Mennad                                #
# Project Name: Password Strength Checker              #
# File Name: main.py                                   #
# Date: 2026-01-24                                     #
# Github Username: pchstpch                            #
########################################################

from logging import exception
import string
import random
import math

def generatePassphrase(length):
    return 0

def generateString(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(int(length)))
    return password

def generatePassword(length, mode):
    if mode == 1:
        passphrase = generatePassphrase(length)
        return passphrase
    elif mode == 2:
        stringPass = generateString(length)
        return stringPass
    else:
        raise Exception("Please enter '1' or '2'")