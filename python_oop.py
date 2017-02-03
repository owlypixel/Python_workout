# Creating simple class with some methods and 2 special functions (init, str)

class Pet():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return self.species

alfred = Pet('Alfred', 'Dog')
print(alfred.getName())
print(alfred)

# check if the property exists
print( hasattr(alfred, 'name'))

# get a property from object:
print(getattr(alfred, 'species'))
