import random

class Crop:
    """A crop class"""
    #make a constructor
    def __init__(self,growth_rate, water_need, light_need):
        self._days_growing = 0
        self._growth = 0
        self._growth_rate = growth_rate
        self._water_need = water_need
        self._light_need = light_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        return {"growth rate":self._growth_rate, "water need: ":self._water_need, "light need: ":self._light_need}

    def reports(self):
        return {"days growing":self._days_growing,"growth: ":self._growth, "status: ":self._status, "type: ":self._type}
        
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    def grows(self, light_need, water_need):
        if light_need >= self._light_need and water_need >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
    


    
    
