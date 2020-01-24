import math


# 1 Given the first three items in a Fibonacci sequence F = [0, 1, 1]
# Create for loop to determine next 20 numbers of the fibonnaci sequence 
# Print F with the final 23 numbers 
# Hint: use F.append() to add a new Fibonnaci value to the end of the list F
def prob1():
	# F = [0, 1]
	# sequence = 0
	# for index, item in enumerate(F):

	# 	if sequence > 0:
	# 		sum = F[index - 1] + F[index]
	# 		F.append(sum)

	# 	sequence += 1
		
	# 	if sequence > 23:
	# 		break

	F = [0, 1]

	for num in range(21):
		sum = F[num] + F[num+1]
		F.append(sum)
	print(F)
	
	# def transform(item0, item1, sequence):
	# 	result = item0 + item1
	# 	return result

	# sequence = 0
	# # *output = *transform 		             *iteration								*filter
	# F = [ result = transform(F[index-1], F[index], sequence) for index, item in enumerate(F) if sequence < 23 ]



# 2 Parenthese are used to preserve order of operations in Python. The 
# following code will add x + y first, then raise to the power of z. This 
# value is assigned g. g = (x+y) ** z
# Given the list x = [2.0, 3.0, 5.0, 7.0, 9.0], create a list Y(x) for each
# float in x. Print the list Y 
def prob2():

	
	x = [2.0, 3.0, 5.0, 7.0, 9.0]

	Yx = [(((3*val)**2)/((99*val) - val**3))-(1/val) for val in x]

	print(Yx)

# 3 General equation for quadratic equation is ax^2 + bx + c = 0
# Create a function to solve the quadratic formula a,b,c
# Return x0, x1 with your function. Use your function to print
# the solution when a = 3.3, b = 1.7, c = -9.4
def prob3():

	def calculate_quad(a, b, c):
		x0 = (-b + math.sqrt((b**2)-(4*a*c)))/(2*a)
		x1 = (-b - math.sqrt((b**2)-(4*a*c)))/(2*a)

		return x0,x1

	x0, x1 = calculate_quad(3.3, 1.7, -9.4)

	print('x0: ', x0)
	print('x1: ', x1)


# 4 Use loop to find the largest integer that when squared is less than 
# 2000. Print the integer
def prob4():
	
	# largest_int = [i**2 for i in range(10000000) if i**2 < 2000]

	# print(largest_int[len(largest_int) - 1])

	largest_int = 0

	while largest_int ** 2 < 2000:
		# print(largest_int)
		largest_int += 1

	largest_int -= 1
	print(largest_int)
	print(largest_int**2)


# 5 Create three seperate functions one calculates volume (v),
# one for surface area (A), and one for density (p) of a sphere
def prob5():
	# r = radius 
	# m = mass

	# calculate volume (v)
	def volume(r):
		v = (4/3)*(math.pi * (r**3))
		return v 

	# calculate area (a)
	def surface_area(r):
		a = 4 * math.pi * (r**2)
		return a 

	# calculate density (p)
	# allow mass m to be optional variable that defaults to m = 0.35
	def density(v, m=0.35):
		p = m / v
		return p


	# print the volume of a sphere with radius r = 0.69
	v = volume(0.69)
	print('volume: ', v)

	# print the surface area of a sphere with radius r = 0.4
	a = surface_area(0.4)
	print('surface area: ', a)

	# print the density of a sphere with r = 0.3 and default mass
	p = density(0.3)
	print('density with default mass: ', p)

	# print the density of a sphere with r = 0.25 and m = 2.0
	p = density(0.25, 2.0)
	print('density: ', p)


	
		

if __name__ == '__main__':
	prob1()
	prob2()
	prob3()
	prob4()
	prob5()