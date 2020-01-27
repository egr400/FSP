#Noah Schmidt, 642383
#EGR400

import math

def main():
	print("PART 1")
	#1
	q1string = "1) One difference between python 2 and 3 is that python 3 requires print\
	statements to include parentheses."

	#2
	print(q1string)
	x = [0, 1, 2, 3, 4, 5, 6]
	print("2) The third item in x is " + str(x[3]))

	#3
	y = x[:]
	y.reverse()
	print("3) " + str(y))

	#4
	z = x[1::2]
	print("4) " + str(z))

	print("5) ")
	#5
	x = 99
	if x > 0:
		print('x is positive')

	print()
	print("PART 2")

	#1
	F = [0, 1, 1]
	while len(F) < 23:
		F.append(nextFib(F[-2:]))
	print("1) " + str(F))

	#2
	x = [2.0, 3.0, 5.0, 7.0, 9.0]
	y = []
	for n in x:
		y.append(nextVal(n))
	print("2) " + str(y))

	#3
	x0, x1 = quadratic(3.3, 1.7, -9.4)
	print("3) X0 is " + str(x0) + ", X1 is " + str(x1))

	#4
	x = 1
	while x**2 < 2000:
		x += 1
	print("4) " + str(x-1))

	#5
	print("5) ")
	print(surfArea(0.4))
	print(density(0.3))
	print(density(0.25, 2.0))



def nextFib(inList):
	return inList[0] + inList[1]

def nextVal(n):
	return (((3.0*n)**2) / ((99*n) - (n**3))) - (1 / n)

def quadratic(a, b, c):
	inner = ((b**2) - (4 * a * c))**(1/2)
	x0 = (-b + inner) / (2 * a)
	x1 = (-b - inner) / (2 * a)
	return x0, x1

def volume(rad):
	return (4/3) * math.pi * (rad**3)

def surfArea(rad):
	return 4 * math.pi * (rad**2)

def density(rad, mass=0.35):
	return mass / volume(rad)

if __name__ == "__main__":
	main()
