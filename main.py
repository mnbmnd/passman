#######################################################################################
# Author: Muneeb Mennad                                                              # 
# Project Name: Passman                                                             #  
# File Name: main.py                                                               #   
# Project Start: 2026-01-24                                                         #  
# Github: https://github.com/mnbmnd                                                  # 
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import menus
import system
import authentication


def run_program():
    menus.splash()

    if not authentication.has_master_credentials():
        menus.setup_menu()
    loginSuccessful = menus.login_menu()
    if loginSuccessful:
        print("\nWelcome,\033[1m", system.whoami(), "\033[0m")
        menus.section_cutter()
        input("Press enter to continue to main menu... ")
        system.clear_screen()
        menus.main_menu()
    else:
        print()
        print("Login Unsuccessful")
        print()
        input("Press enter to exit... ")
        system.exit()


if __name__ == "__main__":
    run_program()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
