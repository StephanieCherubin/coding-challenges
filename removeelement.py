def removeElement(nums, val):
    '''Given an array nums and a value val, remove all instances of that value in-place and return the new length.

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    Clarification:

    Confused why the returned value is an integer but your answer is an array?

    Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.'''
    
    i = 0
    while i < len(nums):
        if nums[i] == val:
            #pop, filter, reduce, del, remove
            # print(nums[i])
            nums.pop(i)
            i -= 1
        i += 1
    return len(nums)
    
        
print(removeElement(nums = [3,2,2,3], val = 3)) # Output: 2, nums = [2,2]
print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)) # 5, nums = [0,1,4,0,3]