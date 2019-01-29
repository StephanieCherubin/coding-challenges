

class BinarySearchTree(object):
    def __init__(self, arg):
        self.arg = arg

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is not None:
                self.left = Node(data)
            else:
                self.left.append(data)

    insert(self, data)
    

