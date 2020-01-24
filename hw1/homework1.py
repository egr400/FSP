"""
Created by Brandon Aldridge on 1/15/2020
HW1 for EGR400
"""

from math import sqrt
from math import trunc
from math import pi


def part1():

    # 1
    print("Python3 uses: {0}, while Python2 uses: {1}"
            .format("print('foo'))", "print 'foo'"))

    # 2
    x = [0, 1, 2, 3, 4, 5, 6]
    print(x[2])

    # 3
    y = x[::-1]
    print(y)

    # 4
    z = x[1:6:2]
    print(z)

    # 5
    # corrections
    x = 99
    if x > 0:
        print('x is positive')


def part2():

    # 1
    print(fibonacci(23))

    # 2
    x_list = [2.0, 3.0, 5.0, 7.0, 9.0]
    y_list = []

    for x in x_list:
        y_list.append(((3.0*x)**2) / (99*x - x**3) - 1/x)

    # 3
    a = 3.3
    b = 1.7
    c = -9.4
    print(quadratic_equation(a, b, c))

    # 4
    # largest square less than 2000
    print((trunc(sqrt(2000)))**2)
    
    # 5
    print(volume(0.69))
    print(density(0.3))
    print(density(0.25, 2.0))


def volume(radius):
    return (4/3) * pi * radius**3


def surface_area(radius):
    return 4 * pi * radius**2


def density(radius, mass=0.35):
    return mass / volume(radius)


def quadratic_equation(a, b, c):
    if a == 0:
        return None
    x_0 = (-b + sqrt(b**2 - 4 *a * c)) / (2 * a)
    x_1 = (-b - sqrt(b**2 - 4 *a * c)) / (2 * a)
    return x_0, x_1


def fibonacci(last_index):
    f = [0, 1, 1]
    for i in range(3, last_index - 1):
        f.append(f[i-1] + f[i-2])
    return f


if __name__ == "__main__":
    part1()
    part2()
