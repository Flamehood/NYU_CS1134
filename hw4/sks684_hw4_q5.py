'''
Simran Soin
CS UY 1134
HW 4 Q5
15 March 2019
'''

#part a
def count_lowercase(s, low, high):
    if high < low:
        return 0
    prev = count_lowercase(s, low+1, high)
    if 97 <= ord(s[low]) and ord(s[low]) <= 122:
        return 1 + prev
    else:
        return prev
        

#part b
def is_number_of_lowercase_even(s, low, high):
    if high < low:
        return None
    prev = is_number_of_lowercase_even(s, low+1, high)
    curr = s[low].islower()
    if prev is None:
        return not(curr)
    if curr is True:
        return not(prev)
    else:
        return prev
    
