# EGR 400 HomeWork-1
# Part 1 of Hw 1
# Question 1
print("Key differences that distinguish python 2 and 3 are the print function, "
      "the way integers get divided, and the Unicode ")
# Question 2
x = [0, 1, 2, 3, 4, 5, 6]
print(x[3])
# Question 3
y = x[::-1]
print(y)
# Question 4
z = x[1::2]
print(z)
# Question 5
# x = 99
# if (x > 0) is true
#     print('x is positive')
x = 99
if x > 0:  # legacy code was missing the colon after the if condition
    print('x is positive')

# Part 2 of Hw 1
# Question 1 use F.append to add a new fibonacccu value to the end of the list
# Fibonacci sequence is defined as F(n) = F(n-1) + F(n-2)

# First three numbers of the sequence is F = [0,1,1]
Fib = [0, 1, 1]
for n in range(2, 22):
    Fib.append(Fib[n] + Fib[n - 1])
    print(Fib)
print(len(Fib))
# Question 2
x = [2.0, 3.0, 5.0, 7.0, 9.0]
Y = []
for n in x:
    math = (((3.0 * n) ** 2) / ((99 * n) - (n) ** 3)) - ((1) / (n))
    Y.append(math)
print(Y)
# Question


def quad_equ(a, b, c):
    sol_1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    sol_2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return sol_1, sol_2


print(quad_equ(3.3, 1.7, -9.4))

# Question 4
x = 0
while x ** 2 < 2000:
    x += 1
print(x - 1)

# Question 5
import math


def volume(r):
    v = (4 / 3) * math.pi * (r ** 3)
    return v


print(volume(.69))


def surface_area(r):
    a = 4 * math.pi * (r ** 2)
    return a


print(surface_area(.4))


def density(vl, m=.35):
    p = m / volume(vl)
    return p


print(density(.3))
print(density(.25, 2.0))
