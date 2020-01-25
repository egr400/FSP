#Homework 2
#Author: Donald Jalving
#EGR 400 Full Stack Development in Python

#Question 1 (Sphere Class)
from math import pi

class sphere:

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def getSphereProperties(self):
        volume = (4/3) * pi * self.radius**3
        surfaceArea = 4 * pi * self.radius**2
        density = self.mass / volume
        return (volume, surfaceArea, density)

red = sphere(1.7, 0.25)
print(dir(red))
print(red.getSphereProperties())