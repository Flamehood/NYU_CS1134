'''
Simran Soin
CS UY 1134
April 19 2019
HW6 Q5
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

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_helper(srt_lnk_lst1, srt_lnk_lst2, s1, s2, merged):
        if s1 == srt_lnk_lst1.trailer and s2 == srt_lnk_lst2.trailer:
            return
        elif s1 == srt_lnk_lst1.trailer:
            merged.add_last(s2.data)
            s2 = s2.next
        elif s2 == srt_lnk_lst2.trailer:
            merged.add_last(s1.data)
            s1 = s1.next
        elif s1.data < s2.data:
            merged.add_last(s1.data)
            s1 = s1.next
        elif s2.data < s1.data:
            merged.add_last(s2.data)
            s2 = s2.next
        elif s2.data == s1.data:
            merged.add_last(s2.data)
            merged.add_last(s1.data)
            s1 = s1.next
            s2 = s2.next
        merge_helper(srt_lnk_lst1, srt_lnk_lst2, s1, s2, merged)
    if srt_lnk_lst1.is_empty():
        return srt_lnk_lst2
    elif srt_lnk_lst2.is_empty():
        return srt_lnk_lst1
    s1 = srt_lnk_lst1.first_node()
    s2 = srt_lnk_lst2.first_node()
    merged = DoublyLinkedList()
    merge_helper(srt_lnk_lst1, srt_lnk_lst2, s1, s2, merged)
    return merged
