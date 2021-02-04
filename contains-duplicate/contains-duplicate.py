class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        else:
            uniqueSet = set()
            uniqueSet.update(nums)
            if len(uniqueSet) == len(nums):
                return False
            return True