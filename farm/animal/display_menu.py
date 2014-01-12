from main_menu import *


def display_menu():
    print()
    print("1. Manual grow, automatically grows for 1 day")
    print("2. Auto grow, automatically grows for 30 days")
    print("3. Report growth")
    print("0. Exit test program")
    print("Please select from the choices above.")
    print()

def get_options():
    is_valid = False
    while not is_valid:
        try:
            choice = int(input("Select option: "))
            if 0 <= choice <= 3:
                is_valid = True
            else:
                print("Invalid selection - please enter between 0 - 3. ")
        except ValueError:
            print("Invalid selection - please enter between 0 - 3. ")
    return choice

def manage_animal(animal):
    noexit = True
    while noexit:
        display_menu()
        choice = get_options()
        if choice == 1:
            manual_grow(animal)
        elif choice == 2:
            auto_grow(animal, 30)
        elif choice == 3:
            print(animal.reports())
        elif choice == 0:
            noexit = False



