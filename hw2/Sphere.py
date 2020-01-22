import math


class Sphere:

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def volume(self):
        return 4 / 3 * math.pi * pow(self.radius, 3)

    def surface_area(self):
        return 4 * math.pi * pow(self.radius, 2)

    def density(self):
        return self.mass / (4 / 3 * math.pi * pow(self.radius, 3))


red = Sphere(1.7, .25)

print(red.volume())
print(red.surface_area())
print(red.density())
