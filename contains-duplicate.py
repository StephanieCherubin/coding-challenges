def containsDuplicate(nums, k):
    '''Given an array of integers, find if the array contains any duplicates.

    Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.'''

    # Check if nums is empty
    # If nums is not empty
        # Create an empty set
        # Add input array into empty set
        # Check length of set against input array
    if not nums:
        return False
    else:
        uniqueSet = set()
        uniqueSet.update(nums)
        if len(uniqueSet) == len(nums):
            return False
        return True
   
        


print(containsDuplicate([], 3)) #false
print(containsDuplicate([1,2,3,1,2,3], 2)) #true