class Crop:
    """A crop class"""
    def __init__(self, growth_rate,light_need, water_need):
        #set the attributes of the class
        self._water_need = water_need
        self._light_need = light_need
        self._status = "Seed"
        self._type = "Generic"
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        
    #set up the modules
    def needs(self):
        return {'light need:':self._light_need, 'water need':self._water_need}

    #method to report and provide information about the crop
    def reports(self):
        return {'type':self._type, 'status':self._status, 'growth':self._growth,'days growing':self._days_growing}

    #method that alters the status attribute depending on the value of growth
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"

    #method that will alter the growth of the crop depending on the value of it
    def grows(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth = self._growth + self._growth_rate
        self._days_growing += 1
        self._update_status()
















        
            
