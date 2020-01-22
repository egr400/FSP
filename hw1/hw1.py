# global variable list
import math
x = [0, 1, 2, 3, 4, 5, 6]


# Part 1
# 1
def differences_in_python():
    answer = "One difference between python2 and 3 is the print statement, within python2 there are multiple ways to " \
             "construct statements. \n" "They can be done with parenthesis surrounding the string literal or no \n" \
             "parenthesis at all, however in python3 this would cause an error."

    print(answer, end="\n")


differences_in_python()


# 2
def print_third_item():

    print(x[3])


print_third_item()


# 3
def reverse_x():

    y = x[::-1]
    print(y)


reverse_x()


# 4
def list_slicing():
    z = x[1::2]

    print(z)


list_slicing()


# 5
def code_correction():
    x = 99
    if (x > 0) is True:
        print('x is positive')
        print("No colon was inserted after if and does not follow Python syntax.")


code_correction()


# Part 2
# 1
def fib_sequence():

    f = [0, 1, 1]
    for i in range(20):
        n = f[i+1] + f[i+2]
        f.append(n)

    print(f)


fib_sequence()


# 2
def power_operation():
    x = [2.0, 3.0, 5.0, 7.0, 9.0]
    Y = []
    for i in x:
        n = (((3.0 * i)**2 / (99 * i - i ** 3)) - 1 / i)
        Y.append(n)
    print(Y)


power_operation()


# 3
def quadratic_equation():

    a = 3.3
    b = 1.7
    c = -9.4

    x0 = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    x1 = ((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)

    print(x0)
    print(x1)


quadratic_equation()


# 4
def find_largest_int():

    x = 1
    while (x+1) ** 2 < 2000:
        x += 1
    print(x)


find_largest_int()


# 5
def calculate_volume(r):

    v = ((4 / 3) * math.pi * r ** 3)
    return v


print(calculate_volume(0.69))


def calculate_surface_area(r):

    A = (4 * math.pi * (r ** 2))
    return A


print(calculate_surface_area(0.4))


def calculate_density(r, m):

    p = (m / calculate_volume(r))
    return p


print(calculate_density(0.3, 0.35))
print(calculate_density(0.25, 2.0))




