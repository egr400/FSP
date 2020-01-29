"""Module which imports mathematical functions"""
import math


class Sphere:
    """Class which creates a sphere based on object's composed elements"""

    def calculate_volume(self):
        """Calculates the volume with the radius given"""
        return (4 / 3) * math.pi * self.radius ** 3

    def calculate_surface_area(self):
        """Calculates the surface area with the radius given"""
        return 4 * math.pi * (self.radius ** 2)

    def calculate_density(self):
        """Calculates the density with the mass given and the volume function"""
        return self.mass / self.calculate_volume()

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = self.calculate_volume()
        self.surface_area = self.calculate_surface_area()
        self.density = self.calculate_density()
