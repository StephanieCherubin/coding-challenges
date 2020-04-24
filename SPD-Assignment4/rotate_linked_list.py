"""Assumptions:

ACTIVITY: Apr 23, Due Apr 30
You're given this problem at a technical interview:
Rotate a given linked list counter-clockwise by k nodes, where k is a given integer.

Singly linked
[A] -> [B] -> [C] , k =8

[A] -> <-[B] -> <- [C] 
What clarifying questions would you ask?

Is this a singly linked list or a doubly linked list



What reasonable assumptions could you state?



What are 2-3 ways you can simplify the problem?
Have just 2 nodes and k = 1



Brainstorm 2-3 ways to approach the problem.
    Find the length
Choose one idea and write pseudocode for it.

"""
# Implement node class
    # Implement linked list
    # Create a length helper function
    
    
    
    
class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        
    def insert_node(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                current.next = newNode
                self.length += 1
            else:  # if linked list is empty
                self.head = newNode
                self.length = 1
            
    def size(self, data):
        return self.length
    
    def rotate(self, k):
        
        # find out the length of linked list
        # Divide length by k (k/self.length)
        # Use modulo for remainder
        # modulo result  = amount of times to shift to left
        # return new linked list
        remainder = self.length % k
        
        
LL = LinkedList() # initialize an empty linked list
LL.insert_node(3)
LL.insert_node(4)     # Linked List Looks like this: [3] -> [4]
print(LL.head.data)
