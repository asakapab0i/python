from crop_class import *

class Wheat(Crop):
    """A potato crop"""
    
    #make a constructor
    def __init__(self):
        Crop.__init__(self,1,3,6)
        self._type = "Wheat"
    
    def grows(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
