''''Fully solve the below linked lists problem in real working code. Use your idea sketches and pseudocode from class, type it in your code editor, run some test cases, and debug your code so it works correctly. Implement at least one solution for 2 or more of the problems below.

Rotate a given singly-linked list counter-clockwise by k nodes, where k is a given integer.
Example: If the given linked list is A → B → C → D → E → F and k is 4, nodes should be modified so the list becomes E → F → A → B → C → D.
Assumptions: k is positive and smaller than n, the length of the linked list.

'''

'''2-3 ways you can simplify the problem'''
# Solve for the base case with k = length
# Have just 2 nodes and k = 1




'''Methods to approach the problem.'''
# Method 1
# To not duplicate the number of rotations 
# and return an answer quicker:
    # if k is more than length.
        # if k is equal to  length, return the same linked list.
        # k > length  rotating by k == k%length
    # if modulo of length/k is less than k,
        # set k to modulo, subtract value of k from length.
        
'''Pseudocode'''

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
            
        # if not head  or  k == 0: # if head does not exist
        #     return head
        
        # find out the length of linked list
        # Divide length by k (k/self.length)
        # Use modulo for remainder
        # modulo result  = amount of times to shift to left
        # return new linked list
        # remainder = self.length % k
        
        if not head or k==0: # if head doesn't exist or if rotation amount is 0.
            return head
        
        # finding the length of list and last node to connect
        self.length = 0
        tail = head
        while tail.next:
            self.length+= 1
            tail = tail.next
        
        # set the new value for k to be the mod of k and the length +1
        k = k%(self.length+1)
        
        # if mod rotation equal to length then return 
        if k == (self.length+1):
            return head
        
        # otherwise find the new head
        newhead= head
        i = 0
        while i < self.length-k:
            newhead = newhead.next
            i+= 1
        
        # reconnect the list to make the rotation
        tail.next = head
        head = newhead.next
        newhead.next = None
        
        return head
        
        
LL = LinkedList() # initialize an empty linked list
LL.insert_node(3)
LL.insert_node(4)     # Linked List Looks like this: [3] -> [4]
print(LL.head.data)
