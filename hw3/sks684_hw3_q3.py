'''
Simran Soin
CS-UY 1134
Homework 3 Q3
'''
def find_duplicates(lst):
    counts_of_all_ints = {}
    for i in lst:
        if i not in counts_of_all_ints:
            counts_of_all_ints[i] = 0
        else:
            counts_of_all_ints[i] += 1
    duplicates = [e for e in counts_of_all_ints if counts_of_all_ints[e] > 0]
    return duplicates


#part b
#worst case run time is O(n)
