# ------- PART ONE ---------

# Question 1
print("Python 2 lets you print without using (), while in Python 3 you must use print()")

# Question 2
x = [0, 1, 2, 3, 4, 5, 6]
print(x[3])

# Question 3
y = x[::-1]
print(y)

# Question 4
z = x[1: 6: 2]
print(z)

# Question 5
x = 99
if x > 0 is True:
    print('x is positive')



# ------- PART TWO --------

# Question 1
F = [0, 1, 1]

for n in range(2, 22):
    F.append(F[n] + F[n - 1])
print(F)

# Question 2
x1 = [2.0, 3.0, 5.0, 7.0, 9.0]


def equation(x):
    return (3.0 * x) ** 2 / (99 * x - x ** 3) - 1 / x


y = list(map(equation, x1))
print(y)

# Question 3
import math


def quadratic(a=3.3, b=1.7, c=-9.4):
    d = dict()
    d["x0"] = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    d["x1"] = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)

    return d


print(quadratic())

# Question 4
n = 1
while n ** 2 < 2000:
    n += 1
print(n - 1)

# Question 5

pi = math.pi


def volume(r=0.69):
    return (4 / 3 * pi) * (r ** 3)


print(volume())


def area(r=0.4):
    return (4 * pi) * (r ** 2)


print(area())


def density(r=0.3, m=0.35):
    return m / volume(r)


print(density())
print(density(0.25, 2.0))
