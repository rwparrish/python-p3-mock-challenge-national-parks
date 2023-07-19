import ipdb

class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._national_parks = []
        
        Visitor.all.append(self)
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Farty Pants")

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
            

    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        pass