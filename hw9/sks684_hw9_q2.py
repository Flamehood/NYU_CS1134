def intersection_list(lst1, lst2):
    intersection = []
    for i in lst1:
        if i in lst2:
            intersection.append(i)
    return intersection
