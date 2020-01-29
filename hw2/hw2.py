import math


class sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_sphere_volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def get_sphere_surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_density_of_sphere(self):
        return self.mass / self.get_sphere_volume()


red = sphere(1.7, 0.25)
print(red.get_sphere_volume())
print(red.get_sphere_surface_area())
print(red.get_density_of_sphere())

x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
for i in range(0, len(x)):
    print(*x[i], sep=' & ')
