class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
            #pop, filter, reduce, del, remove
            # print(nums[i])
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)