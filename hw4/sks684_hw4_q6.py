'''
Simran Soin
CS UY 1134
HW 4 Q5
15 March 2019
'''
def appearances(s, low, high):
    if high < low:
        return {}
    old_dict = appearances(s, low+1, high)
    if s[low] not in old_dict:
        old_dict[s[low]] = 1
    else:
        old_dict[s[low]] += 1
    return old_dict
