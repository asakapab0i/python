from potato_class import *
from main_app import *

def main():
    potato_crop = Potato()
    print(potato_crop.reports())
    #manual grow the crop
    manual_grow(potato_crop)
    print(potato_crop.reports())
    manual_grow(potato_crop)
    print(potato_crop.reports())
    
    
if __name__ == "__main__":
    main()
