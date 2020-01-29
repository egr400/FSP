import math


class Sphere:

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 1.25 * math.pi * radius ** 3
        self.surface_area = 4 * math.pi * radius ** 2
        self.density = mass / self.volume

