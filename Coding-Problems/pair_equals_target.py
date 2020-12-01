# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: 
    # Input: input_array=[5, 3, 6, 8, 2, 4, 7], target=10
    # Ouput:  [3, 7] or [6, 4] or [8, 2]
input_array = [5, 3, 6, 8, 2, 4, 7] 
target = 10

def pairEqualsTarget(input_array, target):
      
    # Create an empty hash set 
    s = set()
      
    for i in range(len(input_array)): 
        pair = target-input_array[i] 
        if (pair in s): 
            print([input_array[i], pair])
        s.add(input_array[i]) 
  
pairEqualsTarget(input_array, target) 


def numbers_equal_target_sum(input_array, target):
    count = 0
    for n in range(len(input_array)):
        for i in range(n + 1, len(input_array)):
            if input_array[n] + input_array[i]== t:
                count += 1
    print(input_array[n] + input_array[i])
            
print(numbers_equal_target_sum(input_array, target))