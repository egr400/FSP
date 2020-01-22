#Question 1
F = [0, 1, 1]
for i in range(3, 23):
    F.append(F[i-1] + F[i-2])
print(F)

#Question 2
x = [2.0, 3.0, 5.0, 7.0, 9.0]
y = []
for i in range(5) :
    y.append((3 * x[i])**2 / ((99 * x[i]) - (x[i]**3)) - (1/x[i]))
print (y)

#Question 3
def quadratic_formula(a, b, c):
    x0 = ((-b + (b**2 - (4 *a *c))**0.5) / (2 *a))
    x1 = ((-b - (b**2 - (4 *a *c))**0.5) / (2 *a))
    return x0, x1

a = 3.3
b = 1.7
c = -9.4
print(quadratic_formula(a, b, c))

#Question 4
while (i**2) < 2000:
    i = i + 1
print (i-1)

#Question 5
def volume(r):
    v = (4/3) * 3.14 * r**3
    return v

def surfaceArea(r):
    A = 4 * 3.14 * r**2
    return A

def density(r, m = 0.35):
    v = volume(r)
    p = m/v
    return p

print(volume(0.69))
print(surfaceArea(0.4))
print(density(0.3))
print(density(0.25, 2.0))
