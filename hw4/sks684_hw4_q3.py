'''
Simran Soin
CS UY 1134
HW 4 Q3
15 March 2019
'''

#part a
def print_triangle(n):
    if n == 0:
        return
    print_triangle(n-1)
    print("*"*n)

#part b
def print_opposite_triangles(n):
    if n == 0:
        return
    print("*"*n)
    print_opposite_triangles(n-1)
    print("*"*n)

#part c
def print_ruler(n):
    if n == 0:
        return
    print_ruler(n-1)
    print("-"*n)
    print_ruler(n-1)
print_ruler(4)
