class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, iterable = None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable is not None:
            for item in iterable:
                self.append(item)
    
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
    
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next
        

    def reverse_linked_list(head):
        previous = None
        return reverse(previous, head)


    def reverse(previous, head):
        if head is None:
            return previous

            next = head.next
            head.next = previous
            previous = head
            head = next
            return reverse(previous, head)

# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print("Given Linked List")
llist.printList() 
llist.reverse() 
print("\nReversed Linked List")
llist.printList() 

