from crop_class import *
import random

def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                option_valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def display_menu():
    print("1. Grow manually over 1 day")
    print("1. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please select an option from the above menu")

def manage_crop(crop):
    print("This is the Crop Management Program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop, 30)
        elif option == 3:
            print(crop.reports())
        elif option == 0:
            noexit = False

    print("Thank you for using Crop Management Program")
    

def manual_grow(crop):
    #set up the valid
    valid = False

    while not valid:
        try:
            light = int(raw_input("Please enter the value of light: ")) 
            if 1 <= light <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")
    #set up the valid
    valid = False
    while not valid:
        try:
            water = int(raw_input("Please enter the value of water: "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except ValueError:
            print("Value entered not valid - please enter a value between 1 and 10")

    #grow the crop
    crop.grows(light, water)
    

def auto_grow(crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grows(light, water)
    

def main():
   
    new_crop = Crop(1,2,2)
    manage_crop(new_crop)
    #print(new_crop.needs())
    #print(new_crop.reports())
    #manual_grow(new_crop)
    #auto_grow(new_crop, 30)
    #new_crop.grows(4,5)
    #print(new_crop.reports())

if __name__ == "__main__":
    main()
