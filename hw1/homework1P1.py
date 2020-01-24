# 1 print the differences in Python2 and Python3
def prob1():
	print('''

	-Python3 is continually adding new features
	 and fixing bugs into the future. 
	 Python2 is obsolete as of this year.

	 -Python3 print syntax is print("Hello")
	 Python2 print syntax is print "Hello"

	-Integer Division in Python3 gives decimals
	when there is a remainder where in Python2 
	it just rounds to nearest whole number

	 ''')

# 2 Given list x print third item in the list
def prob2():
	x = [0, 1, 2, 3, 4, 5, 6]
	print(x[2])
	return x

# 3 Assign y as reversed order of list x. Print y
def prob3(x):
	y = x[::-1] # reverse list by slicing it, counting in -1
	print(y)

# 4 Use list slicing to assign z [1, 3, 5] from x. Print z
def prob4(x):
	z = x[1::2] # we start at index 1 and slice out in 2s 
	print(z)

# 5 Debug your friends code
def prob5():
    x = 90
    if x > 0:
        print('x is positive')

if __name__ == '__main__':
	prob1()
	x = prob2()
	prob3(x)
	prob4(x)
	prob5()