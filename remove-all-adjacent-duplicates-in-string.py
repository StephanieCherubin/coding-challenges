class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if not self.items == []:
            return self.items[-1]
    
    def getStack(self):
        return self.items
        
        
def removeDuplicates(S):
    "Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them. We repeatedly make duplicate removals on S until we no longer can. Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique."

    # Create stack
    
    characterStack = Stack()   
    
    # Iterate over every character in S
    for character in S:
        
        # If next character is same as top of stack (peek),
        if character == characterStack.peek():
         # remove last character by popping
            characterStack.pop()
            continue
        # Else:
        else:
            # Add to stack
            characterStack.push(character)
    return ''.join(characterStack.getStack())

print(removeDuplicates("abbaca")) # Output: ca
print(removeDuplicates("8437358333"))
