'''
Simran Soin
CS UY 1134
HW 4 Q7
15 March 2019
'''
def split_by_sign(lst, low, high):
    if low >= high:
        return
    if lst[low] > 0 and lst[high] < 1:
        lst[low], lst[high] = lst[high], lst[low]
        return split_by_sign(lst, low+1, high-1)
    if lst[high] > 0:
        return split_by_sign(lst, low, high-1)
    if lst[low] < 1:
        return split_by_sign(lst, low+1, high)
