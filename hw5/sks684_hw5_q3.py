'''
Simran Soin
CS 1134
HW 5 Q3
'''
class ArrayDeque():
    INIT_CAPACITY = 8
    def __init__(self):
        self.data = [None] * ArrayDeque.INIT_CAPACITY
        self.num_of_items = 0
        self.front = None
        self.back = None

    def __len__(self):
        return self.num_of_items

    def is_empty(self):
        if self.num_of_items == 0:
            return True
        return False

    def first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data[self.back]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None]*new_cap
        old_index = self.front
        for new_index in range(self.num_of_items):
            self.data[new_index] = old_data[old_index]
            old_index = (old_index + 1) % len(old_data)
        self.front = 0
        self.back = self.front + self.num_of_items - 1

    def enqueue_first(self, elem):
        if (self.num_of_items == len(self.data)):
            self.resize(2*len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front = 0
            self.back = 0
            self.num_of_items = 1
        else:
            self.front = (self.front -1) % len(self.data)
            self.data[self.front] = elem
            self.num_of_items += 1

    def enqueue_last(self, elem):
        if (self.num_of_items == len(self.data)):
            self.resize(2*len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front = 0
            self.back = 0
            self.num_of_items += 1
        else:
            self.back = (self.back + 1) % len(self.data)
            self.data[self.back] = elem
            self.num_of_items += 1

    def dequeue_first(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.num_of_items -= 1
        if self.is_empty():
            self.front = None
            self.back = None
        elif self.num_of_items < len(self.data)//4:
            self.resize(len(self.data)//2)
        return value

    def dequeue_last(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        value = self.data[self.back]
        self.data[self.back] = None
        self.back = (self.back - 1) % len(self.data)
        self.num_of_items -= 1
        if self.is_empty():
            self.front = None
            self.back = None
        elif self.num_of_items < len(self.data)//4:
            self.resize(len(self.data)//2)
        return value
    
    
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

class MidStack:
    def __init__(self):
        self.bottom_half = ArrayStack()
        self.top_half = ArrayDeque()
        self.num_elems = len(self.bottom_half) + len(self.top_half)

    def __len__(self):
        return self.num_elems

    def is_empty(self):
        
        return (self.num_elems == 0)

    def push(self, item):
        if self.is_empty():
            self.bottom_half.push(item)
        else:
            self.top_half.enqueue_first(item)
        self.num_elems += 1
            
    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.top_half) == 0:
            self.num_elems -= 1
            return self.bottom_half.pop()
        else:
            self.num_elems -= 1
            return self.top_half.dequeue_first()

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.top_half) == 0:
            return self.bottom_half.top()
        else:
            return self.top_half.first()

    def mid_push(self, item):
        if self.is_empty():
            self.num_elems += 1
            self.bottom_half.push(item)
        else:
            while len(self.top_half) != (len(self)//2):
                self.bottom_half.push(self.top_half.dequeue_last())
            self.num_elems += 1
            self.bottom_half.push(item)
