def findKthPositive(arr, k):
    '''Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array. '''

    # Create an empty new list to hold missing number
    missing_num = []
    # Loop through input array
    counter = 1
    for num in arr:
        if num != counter:
            missing_num.append(counter)
            print('num:', num, 'counter:',counter)
        counter += 1
    # print('missing num:', missing_num)
        # Compare number from input array to first list
        # If a number is not in input array, add to new list
        # Return number in missing number array at index k + 1
    
    
    
# print(findKthPositive(arr = [2,3,4,7,11], k = 5))
# print(findKthPositive(arr = [1,2,3,4], k = 2))



def missing_num2(arr,k):
    # num_range = [x for x in range(1, max(arr)+1)]
    num_range = []
    for num in range(1,max(arr)+1): #O(n) 
          num_range.append(num)

      
    missing_nums = []

    for num in num_range: # O(n)
        if num not in arr:
            missing_nums.append(num)
    print(missing_nums)
    

    # Check if list empty 
    if not missing_nums:
        return k + len(arr)

    # If list isn't empty 
    else:
        variable = k - len(missing_nums) 
        return missing_nums[-1] + variable
      # return missing_nums[-1] + k-(len(missing_nums))
    
    
    

  


# print(missing_num2(arr = [2,3,4,7,11], k = 5)) # 9
# print(missing_num2(arr = [1,2,3,4], k = 2)) # 6 
print(missing_num2([5,6,7,8,9], 9)) # 14
print(missing_num2([1,2,6,7,8,9], 9)) # 11

