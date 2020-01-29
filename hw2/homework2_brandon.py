"""
Created by Brandon Aldridge on 1/22/2020
hw2 for EGR400
"""

from homework1_brandon import volume, surface_area, density

class Sphere():

    def __init__(self, r, m):
        super().__init__()
        self.radius = r
        self.mass = m
        self.volume = volume(r)
        self.surface_area = surface_area(r)
        self.density = density(r, m)

if __name__ == '__main__':
    red = Sphere(1.7, 0.25)
    print('dir(red): {}'.format(dir(red)))
    print('volume: {}'.format(red.volume))
    print('surface area: {}'.format(red.surface_area))
    print('density: {}'.format(red.density))

    x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11],
         [12, 13, 14, 15]]
    for y in x:
        print(*y, sep='&')
