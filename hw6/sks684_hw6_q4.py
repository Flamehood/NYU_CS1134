'''
Simran Soin
CS UY 1134
April 19 2019
HW6 Q4
'''
from copy import deepcopy
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


def copy_linked_list(lnk_lst):
    copy_lst = DoublyLinkedList()
    og_node = lnk_lst.first_node()
    copy_node = copy_lst.header
    for i in range(len(lnk_lst)):
        copy_next = copy_node.next
        new_node = DoublyLinkedList.Node(og_node.data, copy_node, copy_next)
        copy_node.next = new_node
        copy_next.prev = new_node
        copy_lst.size += 1
        copy_node = copy_node.next
        og_node = og_node.next
    return copy_lst

def deep_copy_linked_list(lnk_lst):
    copy_lst = DoublyLinkedList()
    starting_node = lnk_lst.first_node()
    while starting_node != lnk_lst.trailer:
        if type(starting_node.data) != int:
            sub_list_copy = deep_copy_linked_list(starting_node.data)
            copy_lst.add_last(sub_list_copy)
        else:
            copy_lst.add_last(starting_node.data)
        starting_node = starting_node.next
    return copy_lst
