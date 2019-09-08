import ctypes;
def make_array(n):
    return (n* ctypes.py_object)();

class ArrayQueue:
    INITIAL_CAPACITY=8;
    def __init__(self):
        self.data = make_array(ArrayQueue.INITIAL_CAPACITY);
        self.num_of_elements=0;
        self.front_ind=None;
    def __len__(self):
        return self.num_of_elements;

    def is_empty(self):
        return (self.num_of_elements==0);

    def enqueue(self, item):
        if (self.num_of_elements == len(self.data)):
            self.resize(2*len(self.data));
        if (self.is_empty()):
            self.data[0] = item;
            self.num_of_elements+=1;
            self.front_ind = 0;
        else:
            back_ind = (self.front_ind+self.num_of_elements)%len(self.data);
            self.data[back_ind] = item;
            self.num_of_elements+=1;
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty");
        return self.data[self.front_ind];

    def resize(self,new_cap):
        new_data = make_array(new_cap);
        old_ind = self.front_ind;
        for new_ind in range(self.num_of_elements):
            new_data[new_ind] = self.data[old_ind];
            '''old_ind +=1;
            if old_ind ==len(self.data):
                old_ind = 0;'''
            old_ind = (old_ind+1) % len(self.data);
        self.data = new_data;
        self.front_ind=0;
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty");
        retval = self.data[self.front_ind];
        self.data[self.front_ind]=None; #optional
        self.front_ind = (self.front_ind+1) % len(self.data);
        self.num_of_elements-=1;
        if (self.is_empty()):
            self.front_ind=None;
        elif(self.num_of_elements < len(self.data)//4):
            self.resize(len(self.data)//2);
        return retval;
    
