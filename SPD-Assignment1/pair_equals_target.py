# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: 
    # Input: a=[5, 3, 6, 8, 2, 4, 7], t=10
    # Ouput:  [3, 7] or [6, 4] or [8, 2]
A = [5, 3, 6, 8, 2, 4, 7] 
t = 10

def pairEqualsTarget(A, t):
      
    # Create an empty hash set 
    s = set()
      
    for i in range(len(A)): 
        pair = t-A[i] 
        if (pair in s): 
            print([A[i], pair])
        s.add(A[i]) 
  
pairEqualsTarget(A, t) 


def numbers_equal_target_sum(A, t):
    count = 0
    for n in range(len(A)):
        for i in range(n + 1, len(A)):
            if A[n] + A[i]== t:
                count += 1
    print(A[n] + A[i])
            
print(numbers_equal_target_sum(A, t))