from crop_class import *

class Potato(Crop):
    """A potato crop"""
    
    #make a constructor
    def __init__(self):
        Crop.__init__(self,1,5,7)
        self._type = "Potato"
    
        
def main():
    potato_crop = Potato()
    print(potato_crop.reports())
    
    
if __name__ == "__main__":
    main()
