# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 22:04:05 2020

@author: Monica
"""
##Homework 1

########PART ONE
##1 
difference = str('2 uses str type ASCII, while 3 uses Unicode')
print("1.1 One difference between python 2 and 3 is that",
      difference)

##2
#given list
x = [0,1,2,3,4,5,6]
#print the third item (n-1)
print('2.1', x[2])

##3
#reverse the list
reversed_list = x[::-1]
#make y the reverse
y= reversed_list
#print y
print('3.1', y)

##4
z= slice(1,6,2)
print('4.1', x[z])

##5
x= 99
if (x> 0) is True:
    print('x is positive')
    
########PART TWO
##1
F = [0,1,1]
for i in range(3,23):
    F.append(F[i-1]+ F[i-2])
    print('1.2', F)
    
##2
x = [2.0, 3.0, 5.0, 7.0, 9.0]
y = []
for i in x:
    y.append(i * 3 ** 2)
    print('2.2', y)

##3
import math
a = 3.3
b = 1.7
c = -9.4

mult_4 = 4 * a * c
b_squared = b** 2
root = math.sqrt(b_squared - mult_4)
denominator = 2 * a
plus = -b + root
sub = -b - root
x0 = plus / denominator
x1 = sub / denominator

print('3.2', x1, x0)

##4
x = 1
while x**2 <= 2000:
    print('4.2',x)
    x += 1
     
##5
import math
def volume():
    r = .69
    
    radius_cubed = r **3
    total_volume = 4 / 3 * math.pi * radius_cubed
    print("the volume of a sphere with a radius of",
          r, "is", total_volume)
    
def surface_area():
    r = .4
    
    radius_squared = r ** 2
    total_SA = 4 * math.pi * radius_squared
    print("the surface area of a sphere with radius of",
          r, "is", total_SA)

def density():
    #copy paste volume(), imput the new r 
    r1 = .3
    m1 = .25
    r2 = .25
    m2 = 2
    radius_cubed1 = r1 **3
    total_volume1 = 4 / 3 * math.pi * radius_cubed1
    density_equation1 = m1 / total_volume1
    radius_cubed2 = r2 **3
    total_volume2 = 4 / 3 * math.pi * radius_cubed2
    density_equation2 = m2 / total_volume2
    print('density of the first:', density_equation1,
          'density of second:', density_equation2)
volume()   
surface_area()
density()