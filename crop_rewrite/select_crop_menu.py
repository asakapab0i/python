from potato_class import *
from wheat_class import *

def display_crop_selection():
    print()
    print("1. Select Potato Crop")
    print("2. Select Wheat Crop")
    print()
    print("Please enter the selected number.")

def crop_selection():
    is_valid = False
    while not is_valid:
        try:
            option_selected = int(input("Select an option (1 - 2): "))
            if option_selected in (1,2):
                is_valid = True
            else:
                print("Invalid selection - please enter 1 or 2.")
        except ValueError:
            print("Invalid selection - please enter 1 or 2.")
    return option_selected

def crop_manage_selection():
    noexit = True
    while noexit:
        display_crop_selection()
        option = crop_selection()

        if option == 1:
            new_crop = Potato()
            return new_crop
        else:
            new_crop = Wheat()
            return new_crop
    
        
