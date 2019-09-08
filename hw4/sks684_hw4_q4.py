'''
Simran Soin
CS UY 1134
HW 4 Q4
15 March 2019
'''

def list_min(lst, low, high):
    if low == high:
        return lst[low]
    if lst[low] < lst[high]:
        return list_min(lst, low, high-1)
    elif lst[high] < lst[low]:
        return list_min(lst, low+1, high)
