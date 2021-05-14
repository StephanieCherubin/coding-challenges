class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
      # create index variable 
        i = 0
      # loop thru nums
        while i < len(nums):
        # insert each num at corresponding index
            output.insert(index[i], nums[i])
            i += 1
        return output