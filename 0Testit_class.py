# Define and use a class
from samwise import pb

class Person:
    def __init__(self, name):
        self.name = name

m = Person('Michael')

pb(f"{m.name}","Define Class, instantiate it & Use instantiated obj.name attribute")

