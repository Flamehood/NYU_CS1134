import random
from UnsortedArrayMap import UnsortedArrayMap
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
    

class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        self.table = [UnsortedArrayMap() for i in range(self.N)]
        self.n = 0
        self.queue = ArrayQueue()
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1
            self.queue.enqueue(key)
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for i in range(len(self)):
            val = self.queue.dequeue()
            yield val
            self.queue.enqueue(val)

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()

