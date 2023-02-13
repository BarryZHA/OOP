import random


class Flies: 

    def __init__(self,n): 
        self.name = n 
        self.wings = w 
        self.legs = 4 
        self.flight = 0

    def flight_length(self): 
        self.flight = random.randint(1,10)

    def get_miles(self): 
        return self.flight
    
    def get_name(self):
        return self.name

