# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: 
    # Input: a=[5, 3, 6, 8, 2, 4, 7], t=10
    # Ouput:  [3, 7] or [6, 4] or [8, 2]

def pairEqualsTarget(arr, t):
      
    # Create an empty hash set 
    s = set()
      
    for i in range(0, len(arr)): 
        pair = t-arr[i] 
        if (pair in s): 
            print([arr[i], pair])
        s.add(arr[i]) 
  
A = [5, 3, 6, 8, 2, 4, 7] 
n = 10
pairEqualsTarget(A, n) 