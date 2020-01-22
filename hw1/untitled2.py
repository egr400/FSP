# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:51:19 2020

@author: zhyzm
"""
'''
#1
def fib_loop(n):
    a, b = 0, 1
    for i in range(n+1) :
        a, b = b, a+b
    return a

for i in range(23):
    print(fib_loop(i-1), end=' ')
'''
'''
#2
x = [2.0,3.0,5.0,7.0,9.0]
y = [(3.0*i)**2/(99*i-i**3)-1/i for i in x]
print(y)
'''
'''
#3
import math
a = 3.3
b = 1.7
c = -9.4

d = (b**2) - (4*a*c)

sol1 = (-b-math.sqrt(d))/(2*a) 
sol2 = (-b-math.sqrt(d))/(2*a) 

print("x1=",sol1,"x2=",sol2)
'''
'''
#4
ans = 0
while ans**2 < 2000:
     ans += 1
ans -= 1
print (ans)
'''
'''
#5
import math
def volume(r):

    return 4 / 3 * math.pi * r ** 3

def surface_area(r):

    return 4 * math.pi * r ** 2

def density(r, m=0.35):

    return m / volume(r)

print(volume(0.69))

print(surface_area(0.4))

print(density(0.3))

print(density(0.25, m=2.0))


