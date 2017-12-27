class Animal(object):
    """Makes cute animals."""
    is_alive = True #class member variables.  acts like a default constructor
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Chad", 7)
hippo.description()

sloth = Animal("slothy", 9)
ocelot = Animal("oceloty", 13)

print sloth.is_alive
print hippo.health
print sloth.health
print ocelot.health
