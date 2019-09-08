'''
Simran Soin
CS 1134
HW5 Q5
'''
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if(self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data.pop()

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1]

class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if(self.num_of_elems == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data_arr)
            self.data_arr[back_ind] = elem
            self.num_of_elems += 1

    def dequeue(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        val = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if(self.is_empty()):
            self.front_ind = None
        if((self.num_of_elems < len(self.data_arr) // 4) and (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return val

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_capacity):
        new_arr = make_array(new_capacity)
        old_arr = self.data_arr
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_arr[new_ind] = old_arr[old_ind]
            old_ind = (old_ind + 1) % len(old_arr)
        self.data_arr = new_arr
        self.front_ind = 0

def permutations(lst):
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in lst:
        stack.push(i)
        
    first_elem = []
    first_elem.append(stack.pop())
    queue.enqueue(first_elem)
    while not(stack.is_empty()):
        stack_new_elem = stack.pop()
        for i in range(len(queue)):
            for pos in range(len(queue.first())+1):
                top = queue.first().copy()
                top.insert(pos, stack_new_elem)
                queue.enqueue(top)
            queue.dequeue()
    return queue

perm = permutations([1,2,3])
for i in range(len(perm)):
    print(perm.dequeue())
