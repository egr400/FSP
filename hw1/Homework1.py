print("The print function in Python 3.x requires parenthesis while Python 2.x does not.")

x = [0,1,2,3,4,5,6]
print("x[3]: ", x[3])

y = list(reversed(x))
print("y: " ,*y)

z = x[1:6:2]
print("z: " ,*z)

x = 99 
if (x > 0) is True:
	print('x is positive')

F = [0,1,1]
a = F[-1]
b = F[-2]
for i in range(0,20):
	temp = a
	a = b
	b = temp + b
	F.append(b)
print(*F)

x = [2.0,3.0,5.0,7.0,9.0]
y = [] # y = (((3.0 * i) **2)/(99 * i - i **3)) - (1 / i), where i is input x
for i in x: 
	new = (((3.0 * i) **2)/(99 * i - i **3)) - (1 / i)
	y.append(new)
print(*y, sep = ", ")

a = 3.3
b = 1.7
c = -9.4
x0 = (-b + (b**2 - 4 * a * c)**.5) / (2 * a)
x1 = (-b - (b**2 - 4 * a * c)**.5) / (2 * a)
print(x0, x1, sep = ", ")

i = 1
while(i < 2000):
	if(i**2 < 2000):
		i += 1
	else: 
		print(i - 1)
		break

import math
r = 0.69
v = (4 / 3) * math.pi * r**3
print(v)
r = 0.4
A = 4 * math.pi * r**2
print(A)
r = 0.3
m = 0.35
v = (4 / 3) * math.pi * r**3
rho = m / v
print(rho)
r = 0.25 
m = 2.0
v = (4 / 3) * math.pi * r**3
rho = m / v
print(rho)