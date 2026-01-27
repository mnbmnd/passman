##############################################################################################################################################
# Author: Muneeb Mennad                                                                                                                      #
# Project Name: Password Strength Checker & Generator                                                                                        #
# File Name: main.py                                                                                                                         #
# Project Start: 2026-01-24                                                                                                                  #
# Github Username: pchstpch                                                                                                                  #
#                                                                                                                                            #
##############################################################################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import entropy
import password_generator

def displayMenu():
    print("==================================================================")
    print("==================================================================")
    
    print("PASSWORD STRENGTH CHECKER")
    print("Welcome to Password Strength Checker")
    print()
    userPassword = input("Please enter your password: ")
    print()
    print("Entropy: {:.1f}".format(entropy.getEntropy(userPassword)))
    print("Time to crack (in years): {:.1f}".format(entropy.getTimeToCrack(userPassword)))
    print()
    
    print("==================================================================")
    print("==================================================================")
    
    
    print("PASSWORD GENERATOR")
    print("Welcome to Password Generator!")
    print("Please answer the questions below to generate a password to your liking")
    print()
    print("How long would you like your password to be? (Enter a number from 8-32)")
    print()
    
    passwordLength = int(input("Answer: "))
    while (passwordLength < 8) | (passwordLength > 32):
        print("Please enter a number between 8 and 32 to continue!")
        print()
        passwordLength = int(input("Answer: "))
        
    print("What kind of password you would like? (Enter '1' or '2')")
    print()
    print("1. Passphrase (Easier to remember)")
    print("Example: swell posing gruffly slander onto")
    print()
    print("2. Random String (Alphanumeric)")
    print("Example: a9Fq7XrL2mP8ZKcE")
    print()
    # TODO: Add a 3rd option as 3. Random String (Alphanumeric + Symbols)
    passwordMode = int(input("Answer: "))
    generatedPassword = password_generator.generatePassword(passwordLength, passwordMode)
    
    print("Your generated password is: " + generatedPassword)

if __name__ == "__main__":
    displayMenu()
        
# end main
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #