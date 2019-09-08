'''
Simran Soin
CS 1134
HW 5 Q2
'''
class MaxStack:
    def __init__(self):
        self.data = []
        self.maximum = None

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def push(self, item):
        self.data.append((item, self.maximum))
        if self.maximum == None or item > self.maximum:
            self.maximum = item

    def pop(self):
        if(self.is_empty() == True):
            raise Exception("Stack is empty")
        retval = self.data.pop()
        self.maximum = retval[1]
        return retval[0]

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.data[-1][0]

    def max(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty")
        return self.maximum




