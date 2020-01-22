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
blue = Sphere(2.0, .2)

print(dir(red))
print(red.volume())
print(red.surface_area())
print(red.density())

# Question 2

x = [[0,1,2,3], [4,5,6,7], [8,9,10,11], [12,13,14,15]]

for li in x:
    print(*li, sep=" & ")