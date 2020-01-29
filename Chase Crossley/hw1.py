import math
# global variables
x = [0, 1, 2, 3, 4, 5, 6]

# Part 1


# 1
def one_difference_between_python2_and_python3():
    answer1 = "One difference is in Python2 you do not need the '()' in order to print. \n" \
          "In Python3 you need the '() in order to print.'"
    print(answer1, end="\n")


# 2
def print_third_item_in_list():
    print(x[2], end="\n")


# 3
def reverse_order_of_list():
    y = x[::-1]
    print(y, end="\n")


# 4
def list_slicing():
    z = x[1::2]
    print(z, end="\n")


# 5
def x_is_positive():
    x = 99
    if (x > 0) is True:
        print('x is positive')


def print_answers_part1():
    one_difference_between_python2_and_python3()
    print_third_item_in_list()
    reverse_order_of_list()
    list_slicing()
    x_is_positive()


# Part II

# 1
def fibonacii_sequence(n=23):
    F = [0, 1, 1]
    for i in range(0, n-3):
        F.append(F[-1] + F[-2])
    print(F, end="\n")


# 2
def create_y_list():
    x = [2.0, 3.0, 5.0, 7.0, 9.0]
    Y = []
    for value in x:
        Y.append((((3.0*value)**2)/((99*value) - (value**3))) - (value**-1))
    print(Y)


# 3
def quadratic_formula(a=3.3, b=1.7, c=-9.4):
    x0 = (-b + ((b**2 - 4*a*c) ** .5))/(2*a)
    x1 = (-b - ((b**2 - 4*a*c) ** .5))/(2*a)
    return x0, x1


# 4
def largest_squared_integer_less_than_2000():
    n = 1
    while (n+1)**2 < 2000:
        n += 1
    print(n)


# 5
def volume(r):
    return (4/3) * (math.pi * (r ** 3))


def area(r):
    return 4 * math.pi * (r ** 2)


def density(r, m=0.35):
    return m / volume(r)


def print_answers_part2():
    fibonacii_sequence()
    create_y_list()
    print(quadratic_formula())
    largest_squared_integer_less_than_2000()
    print(volume(0.69), end="\n")
    print(area(0.4), end="\n")
    print(density(0.3), end="\n")
    print(density(0.25, 2), end="\n")


print_answers_part1()
print_answers_part2()
