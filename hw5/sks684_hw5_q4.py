'''
Simran Soin
CS 1134
HW5 Q4
'''
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


class Queue:
    def __init__(self):
        self.stack = ArrayStack()
        self.holding_stack = ArrayStack()
        self.num_elems = 0
        self.front = None

    def __len__(self):
        return self.num_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        self.num_elems += 1
        self.stack.push(item)
        if self.front == None:
            self.front = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        for elem in range(len(self.stack)):
            self.holding_stack.push(self.stack.pop())
        retval = self.holding_stack.pop()
        if len(self.holding_stack) > 0:
            self.front = self.holding_stack.top()
        else:
            self.front = None
        for elem in range(len(self.holding_stack)):
            self.stack.push(self.holding_stack.pop())
        self.num_elems -= 1
        return retval

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.front
