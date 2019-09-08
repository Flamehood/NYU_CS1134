'''
Simran Soin
CS UY 1134
April 19 2019
HW6 Q3
'''
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
            raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev_node = node
        next_node = node.next
        new_node = DoublyLinkedList.Node(data, prev_node, next_node)
        prev_node.next = new_node
        next_node.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        for i in list(orig_str):
            if self.data.is_empty():
                self.data.add_last((i, 1))
            elif i == self.data.last_node().data[0]:
                self.data.last_node().data = (i, self.data.last_node().data[1]+1)
            else:
                self.data.add_last((i, 1))
        ''' Initializes a CompactString object
        representing the string given in orig_str'''
        

    def __add__(self, other):
        ''' Creates and returns a CompactString object that
        represent the concatenation of self and other,
        also of type CompactString'''
        self_node = self.data.first_node()
        other_node = other.data.first_node()
        sums_strs = DoublyLinkedList()
        for i in range(max(len(self.data), len(other.data))):
            if self_node.data[0] == other_node.data[0]:
                sums_strs.add_last((self_node.data[0], self_node.data[1]+other_node.data[1]))
                self_node = self_node.next
                other_node = other_node.next
            else:
                 break
        while (self_node.data != None or other_node.data != None):
            if other_node.data == None:
                sums_strs.add_last(self_node.data)
                self_node = self_node.next
            elif self_node.data == None:
                sums_strs.add_last(other_node.data)
                other_node = other_node.next
            else:
                sums_strs.add_last(self_node.data)
                sums_strs.add_last(other_node.data)
                self_node = self_node.next
                other_node = other_node.next
        retval = CompactString("A")
        retval.data = sums_strs
        return retval

    def __lt__(self, other):
        ''' returns True if”f self is lexicographically
        less than other, also of type CompactString'''
        self_node = self.data.first_node()
        other_node = other.data.first_node()
        while (self_node != self.data.trailer or other_node != other.data.trailer):
            if self_node == self.data.trailer:
                return True
            if other_node == other.data.trailer:
                return False
            if self_node.data[0] == other_node.data[0]:
                if self_node.data[1] == other_node.data[1]:
                    self_node = self_node.next
                    other_node = other_node.next
                elif self_node.data[1] < other_node.data[1]:
                    return (ord(self_node.next.data[0]) < ord(other_node.data[0]))
                elif other_node.data[1] < self_node.data[1]:
                    return (ord(self_node.data[0]) < ord(other_node.next.data[0]))
            else:
                return (ord(self_node.data[0]) < ord(other_node.data[0]))
        return False
    
    def __le__(self, other):
        ''' returns True if”f self is lexicographically
        less than or equal to other, also of type
        CompactString'''
        self_node = self.data.first_node()
        other_node = other.data.first_node()
        while (self_node != self.data.trailer or other_node!= other.data.trailer):
            if self_node == self.data.trailer:
                return True
            if other_node == other.data.trailer:
                return False
            if self_node.data[0] == other_node.data[0]:
                if self_node.data[1] == other_node.data[1]:
                    self_node = self_node.next
                    other_node = other_node.next
                elif self_node.data[1] < other_node.data[1]:
                    return (ord(self_node.next.data[0]) < ord(other_node.data[0]))
                elif other_node.data[1] < self_node.data[1]:
                    return (ord(self_node.data[0]) < ord(other_node.next.data[0]))
            else:
                return (ord(self_node.data[0]) < ord(other_node.data[0]))
        return True

    def __gt__(self, other):
        ''' returns True if”f self is lexicographically
        greater than other, also of type CompactString'''
        return not(self <= other)
        
    def __ge__(self, other):
        ''' returns True if”f self is lexicographically
        greater than or equal to other, also of type
        CompactString'''
        return not(self < other)

    def __repr__(self):
        ''' Creates and returns the string representation
        (of type str) of self'''
        return str(self.data)
