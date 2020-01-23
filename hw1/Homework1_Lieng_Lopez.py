# By: Malane Lieng and Gregorio Lopez
# Part 1
# Question 1
print("Question 1")
print("Python 3 uses parenthesis to print out text while Python 2 does not use parenthesis to print text.")

# Question 2
print("Question 2")
x = [0, 1, 2, 3, 4, 5, 6]
print(x[2])

# Question 3
print("Question 3")
x.reverse()
y = x
print(y)

# Question 4
print("Question 4")
x.reverse()
z = x[1:6:2]
print(z)

# Question 5
x = 99
if (x < 0) is True:
    print('x is positive')

# Part 2
# Question 1
print("Part 2 Question 1")
nterms = int(input("How many terms of the Fibonacci sequence would you like displayed?"))
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Fibonacci sequence up to ", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

# Question 2
print("Part 2 Question 2")
x = [2.0, 3.0, 5.0, 7.0, 9.0]
ylist = []
i = x[1]
while i <= x[4]:
    y = (((3.0 * i) ** 2 / ((99 * i) - (i ** 3))) - (1 / i))
    ylist.append(y)
    i += 1
i = 0
print(ylist)

# Question 3
print("Part 2 Question 3")
a = float(input("Enter a value for a"))
b = float(input("Enter a value for b"))
c = float(input("Enter a value for c"))

x0 = ((b * -1) + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x1 = ((b * -1) - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print("x0 is")
print(x0)
print("x1 is")
print(x1)

# Question 4
print("Part 2 Question 4")

while i ** 2 < 2000:
    i = i + 1
print(i - 1)

# Question 5
print("Part 2 Question 5")


def volume(r):
    v = (4 / 3) * 3.14 * r ** 3
    return v


def surface_area(r):
    s = 4 * 3.14 * r ** 2
    return s


def density(r, m=0.35):
    p = m / volume(r)
    return p


print("Volume is")
print(volume(0.69))
print("Surface Area is")
print(surface_area(0.4))
print("Density is")
print(density(0.3))
print(density(2.0, 0.25))
