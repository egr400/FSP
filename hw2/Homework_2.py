import math
#Saul Morales & Malane Lieng

#---------Problem 1----------------------------------------------
class sphere:




    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.v = (4/3) * math.pi * (self.radius**3)
        self.a = (4) * math.pi * self.radius * self.radius
        self.d = self.mass / self.v

    def info(self):
        return "Volume: {}; Surface Area: {}; Density: {}".format(self.v,self.a,self.d)
pass

red = sphere(1.7, 0.25)

print(red.info())

#-------------------2 -----------------------------------------
x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10,11], [12, 13, 14, 15]]

for i in x:
    print(*i, sep=" & ")

