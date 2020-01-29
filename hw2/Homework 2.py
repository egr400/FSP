import math


print("Part 1---------------\n")
class Sphere:
    
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def volume(self):
        vol = (4 / 3)*math.pi*(self.radius**3)
        return(vol)

    def area(self):
        area = 4*math.pi*(self.radius**2)
        return(area)

    def density(self):
        p = self.mass / self.volume()
        return(p)


red = Sphere(1.7, 0.25)

print(red.volume())
print(red.area())
print(red.density())
print(dir(red))
print("")

print("Part 2----------------\n")
x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

for i in x:
    print(*i, sep=' & ')
        
    
