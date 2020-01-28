# Rigoberto Gonzalez
# EGR 400 Professor Knisely
# 01/28/2020
# HW 2
import math


# volume
# v = (4/3)*math.pi*r**2
# Area
# A = 4*math.pi*r**2
# Surface Area
# p = mass/ volume

# Question 1
class sphere:

    def __init__(self, radius, mass):
        self.r = radius
        self.m = mass

    def volume(self):
        v = (4 / 3) * math.pi * pow(self.r, 3)
        return v

    def area(self):
        a = 4 * math.pi * math.pow(self.r, 2)
        return a

    def surface_area(self):
        p = self.m / self.volume()
        return p


red = sphere(1.7, .025)
print(red.volume())
print(red.area())
print(red.surface_area())

# Question 2

x = [[0, 1, 2, 3], [4, 5, 6, 7],
     [8, 9, 10, 11], [12, 13, 14, 15]]

for i in x:
    print(*i,  sep=' & ')


