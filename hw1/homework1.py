#####Part 1

#1

print("In Python 2, implicit str type is ASCII. But in Python 3 it is Unicode.")

#2

List = [0, 1, 2, 3, 4, 5, 6]
print(List[2])

#3

y = List.reverse()
print(List)

#4

z = List.reverse()
z = List[1:6:2]
print(z)

#5

#needed colon after code block
#indentation needed in body
x = 99
if (x > 0) is True:
    print('x is positive')

#####Part 2

#1

F = [0, 1, 1]
for i in range(3, 23):
    F.append(F[i-1] + F[i-2])
    print(F)

#2

x = [2.0, 3.0, 5.0, 7.0, 9.0]
y = []
for i in range(5):
    y.append((3.0*x[i])**2 / ((99*x[i]-x[i]**3)) - (1/x[i]))
    print(y)

#3


def quad_formula(a, b, c):
    import math
    #negative root
    x1 = ((-1 * b) - math.sqrt((math.pow(b, 2) - 4*a*c)) / (2*a))

    #positive root
    x0 = ((-1 * b) + math.sqrt((math.pow(b, 2) - 4*a*c)) / (2*a))
    return x0, x1

a = 3.3
b = 1.7
c = -9.4
print(quad_formula(a,b,c))

#4

while i**2 < 2000:
    i += 1
    print(i)

#5
import math

def volume(r):

    v = ((4/3)*math.pi*r**3)
    return v

def surface_area(r):

    A = 4*math.pi*r**2
    return A

def density(r, m = 0.35):
    v = volume(r)
    p = (m/v)
    return p

print(volume(0.69))
print(surface_area(0.4))
print(density(0.3))
print(density(0.25, 2.0))