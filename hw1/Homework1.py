#Part 1
#1.
print("The print function is treated as a statement in python"
      " 2 and it is treated as a method is python 3")
#2.
x = [0,1,2,3,4,5,6]
print(x[2])

#3
y = []
n = [-1]

for n in x[::-1]:
   y.append(n)

print (y)

#4
z = x[1:2] + x[3:4] + x[5:6]

print (z)

#5
x = 99
if (x > 0):
   print("X is Positive")
#PartII

#1
n = 23 #set nth terms
F = [0,0,1] # initial list
N = range(n) #create iterative list
i = 3 # set starting point
for s in N:
      F.append(F[i-1] + F[i-2])
      i+=1

print(F)

#2
x = [2.0 ,3.0,5.0,7.0,9.0]
y =[]
for s in x:
   y.append( ( ( (3.0*s)**2)   / ((99*s) - (s**3))   )
                - (1/s)  )

print (y)

#3
a = 3.3
b = 1.7
c = -9.4

x0 = ((-1*b) + ((b*b)-(4*a*c))**(1/2) ) / (2*a)
x1 = ((-1*b) - ((b*b)-(4*a*c))**(1/2) ) / (2*a)

print (x0 , x1)

#4
squ = 0
T = 2000
p = 0
while squ < T:
     p += 1
     squ = p*p
     if squ > T or squ == T: p-=1

print(p)

#5
m = 0.35

def volume (r):
      return ((4/3) * 3.14159 * (r**3))

def sur_Area (r):
      return (4 * 3.14159 * r * r)

def density (m, v):
      return (m/v)

print(volume(0.69))
print(sur_Area(0.4))
print(density(m,volume(0.3)))
print(density(2.0,volume(0.25)))