def removeDuplicates(nums):
    "Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length."
        # Set a count
        # Loop through each num in array
            # while current number is equal to next number:
                # Increase count by 1
            # if current number is no longer equal to next number (no duplicates):
                # delete from starting index to ending index.
        # return length

    
    count = 0
    isEqual = False 
    index = 1
    for n in nums:
        print(nums)
        if index == len(nums):
            break
        if n == nums[index]:
            isEqual = True
            count += 1
        else:
            isEqual = False
            del nums[n:n + count]
            count = 0
        index += 1

            
            
    
    
    

    
    
    
    
    
    
    
    
    
    
    
  
# print(removeDuplicates(nums=[1,1,2]))
# Output: 2, nums = [1,2]
print(removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
# Output: 5, nums = [0,1,2,3,4]