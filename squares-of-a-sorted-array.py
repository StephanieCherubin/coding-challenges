def sortedSquares(nums):
    "Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."
    # Loop through array.
    output = []
    for n in nums:
        output.append(n**2)
    output.sort()
    return output
        # square each number
    # sort in increasing order
    
    
print(sortedSquares(nums = [-4,-1,0,3,10]))
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
print(sortedSquares(nums = [-7,-3,2,3,11]))
# Output: [4,9,9,49,121]