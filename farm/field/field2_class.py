from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *

class Field:
    """Simulate a field that contains animals and crops"""
    #constructor
    def __init__(self, max_crops, max_animals):
        self._crops = []
        self._animals = []
        self._max_crops = max_crops
        self._max_animals = max_animals

    def add_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False
    
    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

def display_crops(crop_list):
    print()
    print("The following crop are in this field")
    pos = 1
    for crop in crop_list:
        print("{0:>2}.{1}".format(pos, crop.reports()))
        pos+=1
        
def display_animals(animal_list):
    print()
    print("The following animal are in this field")
    pos = 1
    for animal in animal_list:
        print("{0:>2}.{1}".format(pos, animal.reports()))
        pos+=1
    
def main():
    new_field = Field(5,5)
    print(new_field._crops)
    print(new_field._animals)
    new_crop2 = Wheat()
    new_animal2 = Cow()
    new_crop = Potato()
    new_animal = Sheep()
    new_field.add_crop(new_crop)
    new_field.add_animal(new_animal)
    new_field.add_crop(new_crop2)
    new_field.add_animal(new_animal2)
    print(new_field._crops)
    print(new_field._animals)

    print(display_animals(new_field._animals))
    print(display_crops(new_field._crops))

if __name__ == "__main__":
    main()












































    
