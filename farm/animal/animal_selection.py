from display_menu import *

def display_option():
    print()
    print("1. Select Cow Animal")
    print("2. Select Sheep Animal")
    print()
    print("Please select an option above.")

def get_option():
    is_valid = False
    while not is_valid:
        try:
            choice = int(input("Selected option: "))
            if choice in (1,2):
                is_valid = True
            else:
                print("Invalid choice - please enter a value either 1 or 2.")
        except ValueError:
            print("Invalid choice - please enter a value either 1 or 2.")
    return choice

def manage_animal_selection():
    noexit = True
    while noexit:
        display_option()
        choice = get_option()
        if choice == 1:
                animal = Cow()
                return animal
        elif choice == 2:
            animal = Sheep()
            return animal
    return animal


def main():
    new_animal = manage_animal_selection()
    manage_animal(new_animal)
    
if __name__ == "__main__":
    main()
