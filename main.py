#######################################################################################
# Author: Muneeb Mennad                                                              # 
# Project Name: Passman                                                             #  
# File Name: main.py                                                               #   
# Project Start: 2026-01-24                                                         #  
# Github: https://github.com/mnbmnd                                                  # 
#######################################################################################

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
import menus
import authentication


def run_program():
    menus.splash()
    if not authentication.has_master_credentials():
        menus.overview()
        menus.setup_menu()
    loginSuccessful = menus.login_menu()
    if loginSuccessful:
        menus.main_menu()
    else:
        exit()


# Main
if __name__ == "__main__":
    run_program()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# mnbmnd
