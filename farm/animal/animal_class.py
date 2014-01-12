
class Animal:
    """An animal class"""
    #constructor
    def __init__(self, growth_rate,water_need, food_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._water_need = water_need
        self._food_need = food_need
        self._status = "Sperm"
        self._type = "Generic"
        self._name = "Default"

    def needs(self):
        return {"water need: ":self._water_need, "food need: ":self._food_need}

    
    def reports(self):
        return {"days growing: ":self._days_growing,"weight: ":self._weight,"status: ":self._status, "type: ":self._type, "growth: ":self._growth_rate}

    
    def _update_status(self):
        if self._weight > 15:
            self._status = "Old"
        elif self._weight > 10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Baby"
        elif self._weight == 0:
            self._status = "Sperm"

    def grows(self, water, food):
        if water >= self._water_need and food >= self._food_need:
            self._weight = self._weight + 10
        self._days_growing += 1
        self._update_status()

