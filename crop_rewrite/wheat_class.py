from crop_class import *

class Wheat(Crop):
    """A potato class"""
    #constructor
    def __init__(self):
        Crop.__init__(self,2,3,6)
        self._type = "Wheat"

    def grows(self, water_need, light_need):
        if light_need >= self._light_need and water_need >= self._water_need:
            if self._status == "Old":
                self._growth = self._growth + self._growth_rate *  .15
            elif self._status == "Mature":
                self._growth = self._growth + self._growth_rate * .35
            elif self._status == "Young":
                self._growth = self._growth + self._growth_rate * .85
            elif self._status == "Seedling":
                self._growth = self._growth + self._growth_rate * 1
            elif self._status == "Seed":
                self._growth = self._growth + self._growth_rate * 2.5
        self._days_growing += 1
        self._update_status()
                




    
    
