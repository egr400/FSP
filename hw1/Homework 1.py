print("----------Answers for Homework 1 Part 1----------\n")
#Question 1
answer = "One difference between Python 2 and Python 3 is that in Python 2 the print function does not need to be followed by a set of parenthesises where as the print function in Python 3 looks like 'print()'."
print(answer)

#Question 2
x = [0,1,2,3,4,5,6]
print(x[2])

#Question 3
y = x[::-1]
print(y)

#Question 4
z = x
print(z[1:6:2])

#Question 5
x = 99
if (x > 0):
   print("x is positive")

print("")
print("----------Answers for Homework 1 Part 2----------\n")
#Question 1
f = [0,1,1]
for i in range(3,23):
   f.append(f[i-1]+f[i-2])
print(f)

#Question 2
x = [2.0,3.0,5.0,7.0,9.0]
def equation(x):
   return (3.0*x)**2 / (99*x - x**3) - 1/x
y = list(map(equation, x))
print(y)

#Question 3
import math

def quadratic():
   a = 3.3
   b = 1.7
   c = -9.4
   x0 = (-b + math.sqrt(b** 2 - 4*a*c)) / (2*a)
   x1 = (-b - math.sqrt(b** 2 - 4*a*c)) / (2*a)
   
   print(x0)
   print(x1)

quadratic()
   
#Question 4
i = 1
while (i+1)**2 < 2000:
   i += 1
   print(i)

#Question 5
def volume(r = 0.69):
    return (4 / 3*math.pi) * (r**3)
print(volume())

def area(r = 0.4):
    return (4*math.pi) * (r**2)
print(area())


def density_P(r = 0.3, m = 0.35):
    return m / volume(r)
print(density_P())
print(density_P(0.25, 2.0))

