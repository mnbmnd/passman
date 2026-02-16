#######################################################################################
# Author: Muneeb Mennad                                                              # 
# Project Name: Passman                                                             #  
# File Name: menus.py                                                              #   
# Project Start: 2026-01-24                                                         #  
# Github: https://github.com/mnbmnd                                                  # 
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import getpass

import passcheck
import passgen
import system
import authentication


ATTEMPTS = 3


def splash():
    print("Passman")
    overview()
    input("Press enter to continue to setup/login...")
    system.clear_screen()
    

def section(title: str):
    print("=" * 88)
    print(f"\n\033[1m[ {title} ]\033[0m")


def section_cutter():
    print("\n" + ("-" * 88))


def overview():
    section("Overview")
    print("\nWelcome to Passman 👋")
    print("└► A simple to use terminal-based password utility that securely manages your passwords\n")
    print("Features")
    print("- Secure password generation")
    print("- Accurate password entropy indicator")
    section_cutter()


def setup_menu():
    section("Setup")
    print("\nTo get started, set up your master password\n")
    masterCredentials = authentication.create_master_credentials()
    authentication.store_master_credentials(masterCredentials)


def login_menu():
    section("Login") 

    loginPassword = getpass.getpass("\nPassword: ")
    success = authentication.authenticate(loginPassword)
    
    attemptsRemaining = 3
    while (not success) and (attemptsRemaining > 0):
        print("\nPassword incorrect")
        print(f"You have \033[1m{attemptsRemaining}\033[0m attempts remaning!\n")

        loginPassword = getpass.getpass("Password: ")
        success = authentication.authenticate(loginPassword)
        attemptsRemaining -= 1

    return success


def main_menu():
    section("Main Menu")

    print("\n1. Go to Passgen (Generator)")
    print("2. Go to Passcheck (Checker)")
    print("3. Quit\n")


    option = int(input("Ans: "))

    if option == 1:
        system.clear_screen()
        passgen_menu()
    elif option == 2:
        system.clear_screen()
        passcheck_menu()
    elif option == 3:
        system.clear_screen()
        print("Enter 0 to go back or 1 to confirm\n")
        confirmed = int(input("Ans: "))
        if confirmed:
            system.exit()
        else:
            system.clear_screen()
            main_menu()
    

def passgen_menu():
    print("Passgen")
    section("Description")
    
    print("\nPassgen generates new passwords for you using secure randomness.\n")
   
    print("1. Start Passgen")
    print("2. Go back to main menu\n")
    passgenChoice = int(input("Ans: "))
    
    if passgenChoice == 1:
        section_cutter()
        print("Passgen Started\n")
        # \033[1m\033[0m makes text bold
        print("What would you like to generate?\n")
        print(
            "1. A\033[1m Passphrase \033[0m– a sequence of randomly selected words"
        )
        print("└► Example:  \033[1mswell posing gruffly slander onto\033[0m")
        print("")
        print(
            "2. A\033[1m String \033[0m– a random string of letters, numbers, and symbols"
        )
        print("└► Example:  \033[1ma9Fq7XrL2mP8ZKcEi\033[0m\n")
        
        passwordType = int(input("Ans: "))
        generatedPassword = passgen.generatePassword(passwordType)
        
        print("Generated password:\033[1m", generatedPassword, "\033[0m")
        # display_pass_strength(generatedPassword)
    else:
        system.clear_screen()
        main_menu()

    
    


# displays the password strength of an inputted password
def display_pass_strength(generatedPassword=None):
    if generatedPassword is None:
        userPassword = getpass.getpass("Password: ")

        print("Entropy: {:.1f}".format(passcheck.getEntropy(userPassword)))
    else:
        print("Entropy: {:.1f}".format(passcheck.getEntropy(generatedPassword)))
    print()
    print("Learn more: "
        "https://auth0.com/blog/defending-against-password-cracking-understanding-the-math/"
    )


def passcheck_menu():
    print("Password Strength Checker")
    section("Description")
    print(
        "\nThe Password Checker analyzes a password and estimates how secure \n"
        "it is against common attack methods.\n"
    )

    print("It measures:")
    print(
        " 1. Password entropy – a way of quantifying how unpredictable a password \n"
        "is based on its length and the characters used."
    )
    print(
        " 2. Time to crack – an estimate of how long it would \n"
        "take to brute-force the password assuming modern hardware and realistic attack speeds.\n"
    )

    print(
        "Higher entropy generally means more possible combinations, which increases the \n"
        "time required to crack the password. The checker uses this \n"
        "information to give a practical sense of strength rather than \n"
        "a simple “weak/strong” label.\n"
    )

    display_pass_strength()
    print()
    main_menu()
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
