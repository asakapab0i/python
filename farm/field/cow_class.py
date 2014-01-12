from animal_class import *

class Cow(Animal):
    """A cow class"""
    #constructor
    def __init__(self):
        Animal.__init__(self,3,8,8)
        self._type = "Cow"
     

    def grows(self, water, food):
        if water >= self._water_need and food >= self._food_need:
            if self._status == "Old":
                self._weight += 10 * 2
            elif self._status == "Mature":
                self._weight += 20 * 3
            elif self._status == "Young":
                self._weight += 30 * 4
            elif self._status == "Baby":
                self._weight += 40 * 5
            elif self._status == "Sperm":
                self._weight = 10
        self._days_growing += 1
        self._update_status()



