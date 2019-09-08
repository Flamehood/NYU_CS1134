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
    


class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, root):
        if (root is None):
            return 0
        else:
            left_count = self.subtree_count(root.left)
            right_count = self.subtree_count(root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, root):
        if (root is None):
            return 0
        else:
            left_sum = self.subtree_sum(root.left)
            right_sum = self.subtree_sum(root.right)
            return root.data + left_sum + right_sum


    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, root):
        if (root.left is None and root.right is None):
            return 0
        elif (root.left is  None):
            return 1 + self.subtree_height(root.right)
        elif (root.right is  None):
            return 1 + self.subtree_height(root.left)
        else:
            left_height = self.subtree_height(root.left)
            right_height = self.subtree_height(root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, root):
        if(root is None):
            return
        else:
            yield root
            yield from self.subtree_preorder(root.left)
            yield from self.subtree_preorder(root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_postorder(root.left)
            yield from self.subtree_postorder(root.right)
            yield root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, root):
        if(root is None):
            return
        else:
            yield from self.subtree_inorder(root.left)
            yield root
            yield from self.subtree_inorder(root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
                
    def leaves_list(self):
        def leaves_helper(root, node):
            if node.left is None and node.right is None and node!= root:
                yield node.data
            elif node.left is None:
                yield from leaves_helper(root, node.right)
            elif node.right is None:
                yield from leaves_helper(root, node.left)
            else:
                yield from leaves_helper(root, node.left)
                yield from leaves_helper(root, node.right)
        if self.is_empty():
            return []
        return [i for i in leaves_helper(self.root, self.root)]
