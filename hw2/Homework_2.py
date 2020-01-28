import math
# Imports the math library to use the value of pi easily for volume and surface area later

def main():

pi = math.pi


class Sphere:
# Creates a new class name Sphere

    def __init__(self, radius, mass): 
        self.radius = radius
        self.mass = mass
# Defines the initial values for the class Sphere

    def volume(self):
        return float((4 / 3) * pi * self.radius * self.radius * self.radius)
# Defines volume for objects of class Sphere

    def surfacearea(self):
        return float(4 * pi * self.radius * self.radius)
# Defines surfacearea for objects of class Sphere

    def density(self):
        return float(red.mass / red.volume())
# Defines density for objects of class Sphere

red = Sphere(1.7, 0.25)
# Creating the object red as class Sphere

print(red.volume()) 
# Prints the volume of red print(red.surfacearea())
print(red.surfacearea())
# Prints the surface of red
print(red.density())
# Prints the density of red
print(dir(red))
# Prints a list of attributes and methods for the object red 

x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
# Assigning values to lists inside of a bigger list called X

for i in x:
    print(*i, sep=' & ')
# Prints the values in each list in X separated by & and creates a newline inbetween lists

if __name__ == '__main__':
    main()