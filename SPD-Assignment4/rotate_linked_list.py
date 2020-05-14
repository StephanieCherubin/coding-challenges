"""
You're given this problem at a technical interview:
    Rotate a given linked list counter-clockwise by k nodes, where k is a given integer. 
"""


'''1.  What clarifying questions would you ask?'''

    # Clarify the meaning of counter-clockwise on a linkedlist.
    # Is this a singly linked list or a doubly linked list
    # Will k always be positive?
        # What should I do if k is negative?
            # Should I rotate clockwise in that case?
    # Will k always be more than the amount of nodes?

''' 2. What reasonable assumptions could you state?'''
#


'''3. What are 2-3 ways you can simplify the problem?'''
# Solve for the base case with k = length
# Have just 2 nodes and k = 1




'''4. Brainstorm 2-3 ways to approach the problem.'''
# Method 1
# To not duplicate the number of rotations 
# and return an answer quicker:
    # if k is more than length.
        # if k is equal to  length, return the same linked list.
        # k > length  rotating by k == k%length
    # if modulo of length/k is less than k,
        # set k to modulo, subtract value of k from length.
        
'''5. Choose one idea and write pseudocode for it.'''

# Implement node class
    # Implement linked list
    # Create a length helper function
    
    # if k is less than length: 
        # Traverse to find last node         
        # Remove null pointer from last node
        # Point first node to null. 
        # Move first node to end
''' Example 1:
     input: A -> B -> C -> D->E ->null , k = 2
    Explanation:
    rotate 1 steps to the right: E->A->B->C->D->NULL
     rotate 2 steps to the right: D->E->A->B->C->NULL '''
    
'''Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
BRUTE FORCE
Explanation:
rotate 1 step to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL  ''' 

''' USE MODULO of length and k to decrease time complexity
length = 5, k = 4 5%4 =k therefore k = 1
Explanation: 
rotate 1 step to the right: 2->0->1->NULL
 '''
    
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
    
    def rotate(self, head, k):
            
        if not head  or  k == 0: # if head does not exist
            return head
        
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
