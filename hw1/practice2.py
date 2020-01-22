import math
# No.1 Fibonacci Sequence
fib_list = [0, 1, 1]
for num in range(2, 22):
    fib_list.append(fib_list[num - 1] + fib_list[num])
print(fib_list)

# No.2 Order of Operations
given_list = [2.0, 3.0, 5.0, 7.0, 9.0]
produced_list = []
for x in given_list:
    numerator = (3.0 * x) ** 2
    denominator = (99 * x) - (x ** 3)
    simplified = numerator / denominator
    factor = 1 / x
    result = simplified - factor
    produced_list.append(result)
print(produced_list)

# No.3 Quadratic Formula
val_1 = 3.3
val_2 = 1.7
val_3 = -9.4


def quad_formula(element_1, element_2, element_3):
    top = math.sqrt((element_2 ** 2) - (4 * element_1 * element_3))
    bot = 2 * element_1
    result_1 = (-element_2 + top) / bot
    result_2 = (-element_2 - top) / bot
    return result_1, result_2


print(quad_formula(val_1, val_2, val_3))

# No.4 Finding the largest integer that when squared is less than 2000
answer = round(math.sqrt(2000)) - 1
print(answer)
# alternative solution (by looping)
num = 1
while num**2 < 2000:
    num += 1
print(num - 1)

# No.5 Physics


# gets the volume of a sphere given a radius
def volume_of_sphere(radius):
    return (4 / 3) * math.pi * (radius ** 3)


# gets the surface area of the sphere given a radius
def surface_area_of_sphere(radius):
    return 4 * math.pi * (radius ** 2)


# gets the density of a sphere given radius and/or mass
def density_of_sphere(radius, mass=0.35):
    return mass / volume_of_sphere(radius)


print(volume_of_sphere(0.69))
print(surface_area_of_sphere(0.4))
print(density_of_sphere(0.3))
print(density_of_sphere(0.25, 2.0))
