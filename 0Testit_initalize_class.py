# create a class with an attribute, instantiate the object initializing the attribute and reference the attribute
from samwise import pb


class Building:

    def __init__(self, number):
        self.number = number


o_b = Building(235)

pb(o_b.number, "Instantiate an object, and then use attribute")
