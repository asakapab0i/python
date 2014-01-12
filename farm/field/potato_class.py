from crop_class import *

class Potato(Crop):
    """A potato class"""
    #constructor
    def __init__(self):
        Crop.__init__(self,1,3,4)
        self._type = "Potato"

    def grows(self, water_need, light_need):
        if light_need >= self._light_need and water_need >= self._water_need:
            if self._status == "Old":
                self._growth = self._growth + self._growth_rate *  .05
            elif self._status == "Mature":
                self._growth = self._growth + self._growth_rate * .25
            elif self._status == "Young":
                self._growth = self._growth + self._growth_rate * .75
            elif self._status == "Seedling":
                self._growth = self._growth + self._growth_rate * .90
            elif self._status == "Seed":
                self._growth = self._growth + self._growth_rate * 1.5
        self._days_growing += 1
        self._update_status()
                




    
    
