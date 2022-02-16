import random
class Insect:

    def __init__(self,wings,legs):
        self.wings = wings
        self.legs = legs
        self.flight = 0

    def length_of_flight(self):
        self.flight = random.randint(1,10)
    
    def get_flight_length(self):
        return self.flight