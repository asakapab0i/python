from animal_class import *

class Sheep(Animal):
    """A cow class"""
    #constructor
    def __init__(self):
        Animal.__init__(self,2,4,4)
        self._type = "Cow"
     

    def grows(self, water, food):
        if water >= self._water_need and food >= self._food_need:
            if self._status == "Old":
                self._weight += 5 * 2
            elif self._status == "Mature":
                self._weight += 10 * 3
            elif self._status == "Young":
                self._weight += 15 * 4
            elif self._status == "Baby":
                self._weight += 20 * 5
            elif self._status == "Sperm":
                self._weight = 5
        self._days_growing += 1
        self._update_status()

