from cow_class import *
from sheep_class import *
import random



def auto_grow(animal, days):
    for day in range(days):
        water = random.randint(1, 10)
        food = random.randint(1, 10)
        animal.grows(water, food)

def manual_grow(animal):
    is_valid = False
    while not is_valid:
        try:
            water = int(input("Please enter water value: "))
            if 0 <= water <= 10:
                is_valid = True
            else:
                print("Incorrent water value - please enter between 1 to 10. ")
        except:
            print("Incorrent water value - please enter between 1 to 10. ")
    is_valid = False
    while not is_valid:
        try:
            food = int(input("Please enter water value: "))
            if 0 <= food <= 10:
                is_valid = True
            else:
                print("Incorrent food value - please enter between 1 to 10. ")
        except:
            print("Incorrent food value - please enter between 1 to 10. ")
        


