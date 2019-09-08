'''
Simran Soin
CS UY 1134
April 19 2019
HW6 Q2
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

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in list(num_str):
            self.data.add_last(i)
        
    def __add__(self, other):
        longer_num = max(len(self.data), len(other.data))
        sums_str = ""
        starting_self = self.data.trailer
        starting_other = other.data.trailer
        carry_over = 0
        for i in range(longer_num):
            if starting_self.prev.data != None and starting_other.prev.data != None:
                starting_self = starting_self.prev
                starting_other = starting_other.prev
                sum_of_both = str(int(starting_self.data) + int(starting_other.data)+int(carry_over))
                
            elif starting_self.prev.data == None:
                starting_other = starting_other.prev
                sum_of_both = str(int(carry_over) + int(starting_other.data))
                
            elif starting_other.prev.data == None:
                starting_self = starting_self.prev
                sum_of_both = str(int(carry_over) + int(starting_self.data))

            if len(sum_of_both)>1:
                carry_over = sum_of_both[0]
                sums_str = sum_of_both[1] + sums_str
            else:
                carry_over = 0
                sums_str = sum_of_both + sums_str
        if carry_over != 0:
            sums_str = carry_over + sums_str
        while sums_str[0] == "0":
            sums_str = sums_str[1:]
        return Integer(sums_str)

    def __mul__(self, other):
        starting_num = self.data.last_node()
        final_answer = 0
        for i in range(len(self.data)):
            acc = str(0)*i
            other_num = other.data.last_node()
            carry_over = 0
            for e in range(len(other.data)):
                product = str((int(starting_num.data) * int(other_num.data))+int(carry_over))
                if len(product)>1:
                    carry_over = product[0]
                    acc = product[1] + acc
                else:
                    carry_over = 0
                    acc = product + acc
                other_num = other_num.prev
            starting_num = starting_num.prev
            if carry_over != 0:
                acc = carry_over + acc
            final_answer += int(acc)
        return final_answer

    def __repr__(self):
        return "".join([str(item) for item in self.data])
