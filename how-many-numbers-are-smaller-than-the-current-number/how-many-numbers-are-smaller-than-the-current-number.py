class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        nums_sort = sorted(nums)
        for i in nums:
            output.append(nums_sort.index(i))
        return output