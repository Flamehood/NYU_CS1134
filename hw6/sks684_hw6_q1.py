'''
Simran Soin
CS UY 1134
April 19 2019
HW6 Q1
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



class LinkedQueue:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.num_elems = len(self.data)
        
    def __len__(self):
        return self.num_elems

    def is_empty(self):
        return (self.num_elems == 0)

    def enqueue(self, data):
        self.data.add_last(data)
        self.num_elems += 1

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.data.first_node().data

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        self.num_elems -= 1
        return self.data.delete_node(self.data.first_node())
