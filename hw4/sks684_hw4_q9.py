'''
Simran Soin
CS UY 1134
HW 4 Q9
15 March 2019
'''
import math

def permutations(lst, low, high):
    if low == high:
        return [ [ lst[low] ] ]
    old_list = permutations(lst, low, high-1)
    perms = []
    for i in range(len(old_list)):
        for pos in range(len(old_list[i])+1):
            new_perm = old_list[i].copy()
            new_perm.insert(pos, lst[high])
            perms.append(new_perm)
    return perms
