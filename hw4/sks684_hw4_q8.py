'''
Simran Soin
CS UY 1134
HW 4 Q8
15 March 2019
'''

def flat_list(nested_lst, low, high):
    final_lst = []
    for i in range(low, high):
        if isinstance(nested_lst[i], list):
            final_lst += flat_list(nested_lst[i], 0, len(nested_lst[i]))
        else:
            final_lst.append(nested_lst[i])
    return final_lst
