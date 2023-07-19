import ipdb

class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

        NationalPark.all.append(self)
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception("Has Attribute")
        elif isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Farty Pants")
            

    def trips(self, new_trip=None):
        from classes.trip import Trip
        np_trips = [trip for trip in Trip.all if trip._national_park == self]
        return np_trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass