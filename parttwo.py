import math

# =========== Problem 1 ==========
F = [0, 1, 1]
for num in range(2, 22):
    if (num < 2):
        F.append(num)
    else:
        num = F[1] + F[2]
        F[1] = F[2]
        F[2] = num
        print(num)

# =========== Problem 2 ==========
x = [2.0, 3.0, 5.0, 7.0, 9.0]
Y = []

for i in x:
    new_list = (3.0 * i) ** 2 / (99 * i - i ** 3) - 1 / i
    Y.append(new_list)
    print(Y)


# =========== Problem 3 ==========
def quad(a, b, c):
    xo = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return xo, x1


print(quad(a=3.3, b=1.7, c=-9.4))


# =========== Problem 4 ==========
largest = 0
while (not largest ** 2 >= 2000):
    largest += 1
    print(largest-1)



# =========== Problem 5 ==========
def volume(v):
    return 4 / 3 * math.pi * v ** 3


def surface_area(A):
    return 4 * math.pi * A ** 2


def density(r, m=0.35):
    return m / volume(r)


print(volume(0.69))
print(surface_area(0.4))
print(density(0.3))
print(density(0.25, m=2.0))
