def smallerNumbersThanCurrent(nums):
    "Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]. Return the answer in an array."
    
    # Create an output array
    # Create a count
    
    # Loop through nums.
    # while nums[i] < nums[j]:
        # update count by 1.
    # append count to output array
        
    output = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        output.append(count)
    return output
                
            






print(smallerNumbersThanCurrent([8,1,2,2,3])) 
# Output: [4,0,1,1,3]
print(smallerNumbersThanCurrent([7,7,7,7]))
# Output: [0,0,0,0]
print(smallerNumbersThanCurrent([6,5,4,8]))
# Output: [2,1,0,3]