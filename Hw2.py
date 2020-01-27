import math

pi = math.pi


class Sphere:

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def volume(self):
        return float((4 / 3) * pi * self.radius * self.radius * self.radius)

    def surfacearea(self):
        return float(4 * pi * self.radius * self.radius)

    def density(self):
        return float(red.mass / red.volume())


red = Sphere(1.7, 0.25)

print(red.volume())
print(red.surfacearea())
print(red.density())
print(dir(red))

x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

for i in x:
    print(*i, sep=' & ')