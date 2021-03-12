class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        # Create a current sum variable at 0
        curr_sum = nums[0]
        # Loop through nums
        for i in range(1, len(nums)):
            # Current = Add i and i + 1

            # If current sum is > max sum
            max_sum = max(max_sum, nums[i], nums[i]+curr_sum)
            curr_sum = max(nums[i], curr_sum + nums[i])
      #     max_sum = 4
      #     curr_sum = 0
        return max_sum
