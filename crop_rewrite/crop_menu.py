from select_crop_menu import *

import random

def auto_grow(crop, days):
    
    #iterate for how many days given
    
    for day in range(days):
        water = random.randint(1, 10)
        light = random.randint(1, 10)
        crop.grows(light,water)
    
def manual_grow(crop):
    #input light
    is_valid = False
    while not is_valid:
        try:
            light = int(input("Enter light value (1-10): "))
            if 1 <= light <= 10:
                is_valid = True
            else:
                print("Value entered not valid - please enter between 1 to 10.")
        except ValueError:
            print("Value entered not valid - please enter between 1 to 10.")
    #input water
    is_valid = False
    while not is_valid:
        try:
            water = int(input("Enter water value (1-10): "))
            if 1 <= water <= 10:
                is_valid = True
            else:
                print("Value entered not valid - please enter between 1 to 10.")
        except ValueError:
            print("Value entered not valid - please enter between 1 to 10.")

    crop.grows(light, water)
    


def display_menu():
    print()
    print("1. Manual grow, automatically grow for 1 day.")
    print("2. Auto grow, automatically grows for 30 days.")
    print("3. Report Status.")
    print("0. Exit test program.")
    print()
    print("Please choose from above choice.")

def get_menu_option():
    is_valid = False
    while not is_valid:
        try:
            option_selected = int(input("Option selected: "))
            if 0 <= option_selected <= 3:
                is_valid = True
            else:
                print("The value you entered is not valid - pleaes enter between 0 - 3")
        except:
            print("The value you entered is not valid - pleaes enter between 0 - 3")
    return option_selected

def manage_crop(crop):
    noexit = True
    while noexit:
        display_menu()
        option_selected = get_menu_option()
        if option_selected == 1:
            manual_grow(crop)
        elif option_selected == 2:
            auto_grow(crop, 30)
        elif option_selected == 3:
            print(crop.reports())
        elif option_selected == 0:
            noexit = False
            
def main():
    #instantiate the class
    new_crop = Crop(1,4,3)

    crop = crop_manage_selection()
    manage_crop(crop)


if __name__ == "__main__":
    main()
