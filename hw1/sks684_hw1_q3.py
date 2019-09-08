'''
Simran Soin
CS UY 1134
11 February 2019
Homework 1 Question 3
'''

#part a
def sum_of_squares(n):
    sum_of_squares = 0
    for i in range(n):
        sum_of_squares += (i**2)
    return sum_of_squares

#part b
n = 5
sum_of_n_squares = sum([i**2 for i in range(n)])

#part c
def sum_of_odd_squares(n):
    sum_of_odd_squares = 0
    for i in range(n):
        if i%2 == 1:
            sum_of_odd_squares += (i**2)
    return sum_of_odd_squares

#part d
n = 5
sum_of_n_odd_squares = sum([(i**2) for i in range(n) if i%2==1])
print(sum_of_n_odd_squares)
