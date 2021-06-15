class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        # loop thru nums, 
        for num in nums:
            if num != largest:
                if num > largest//2:
                    return -1

        return nums.index(largest)