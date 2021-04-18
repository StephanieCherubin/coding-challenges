class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sortedNums = sorted(nums, reverse=True)
        i = sortedNums[0]
        j = sortedNums[1]
        return (i - 1) * (j - 1)