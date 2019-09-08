'''
Simran Soin
CS-UY 1134
Homework 3 Q4
'''

#part a
#worst case run time is O(n^2)

#partb
def remove_all(lst, value):
    num_shifted = 0
    for e in range(len(lst)):
        if lst[e] == value:
            num_shifted += 1
        if not(lst[e] == value or lst[e-1] == None):
            lst[e], lst[e-num_shifted] = lst[e-num_shifted], lst[e]
    return lst[:(-1*num_shifted)]
