'''
Simran Soin
CS 1134
HW 9 Q3
'''
import random
from UnsortedArrayMap import UnsortedArrayMap

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
        self.table = [None for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if isinstance(curr_bucket, UnsortedArrayMap.Item):
            return curr_bucket.value
        elif curr_bucket is None:
            return None
        else:
            return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            self.table[i] = UnsortedArrayMap.Item(key, value)
            self.n += 1
        elif isinstance(curr_bucket, UnsortedArrayMap.Item):
            if key == curr_bucket.key:
                curr_bucket.value = value
            else:
                first_item = curr_bucket
                curr_bucket = UnsortedArrayMap()
                curr_bucket[first_item.key] = first_item.value
                curr_bucket[key] = value
                self.n += 1
        else:
            old_size = len(curr_bucket)
            curr_bucket[key] = value
            new_size = len(curr_bucket)
            if (new_size > old_size):
                self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if isinstance(curr_bucket, UnsortedArrayMap.Item):
            del curr_bucket
        else:
            del curr_bucket[key]
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if isinstance(curr_bucket, UnsortedArrayMap):
                for key in curr_bucket:
                    yield key
            elif curr_bucket is None:
                continue
            else:
                yield curr_bucket.key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        if curr_bucket is None:
            print(None)
        elif isinstance(curr_bucket, UnsortedArraymap.Item):
            print(curr_bucket.key)
        else:
            for key in curr_bucket:
                print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()
