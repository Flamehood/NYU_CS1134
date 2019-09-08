'''
Simran Soin
CS UY 1134
11 February 2019
Homework 1 Question 5
'''
def fibs(n):
    x = 0
    y = 1
    while n>0:
        yield y
        x, y = y, y+x
        n -= 1

for curr in fibs(8):
    print(curr, end=" ")
