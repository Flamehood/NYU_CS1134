'''
Simran Soin
CS UY 1134
22 February 2019
Homework 2 Question 3
'''

def factors(n):
    for num in range(1, int(n**0.5)+1):
        if n % num == 0:
            yield num
    for num in range(int(n**0.5)-1, 0, -1):
        if n % num == 0:
            yield n//num
