'''
Simran Soin
CS UY 1134
22 February 2019
Homework 2 Question 6
'''

def two_sum(srt_lst, target):
    for i in range(len(srt_lst)):
        if (target - srt_lst[i]) in srt_lst:
            return (i, srt_lst.index(target-srt_lst[i]))
