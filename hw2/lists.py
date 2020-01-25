#Homework 2
#Author: Donald Jalving
#EGR 400 Full Stack Development in Python

#Question 2 (Iterating Through Lists)

x = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9 ,10, 11], [12, 13, 14, 15]];

for i in range(len(x)):
    print(*x[i], sep = ' & ')
