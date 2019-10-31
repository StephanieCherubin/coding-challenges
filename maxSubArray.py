
def maxSubArray(nums):

  current_max_sum = 0
  max_sum = 0

  for i in nums:
    current_max_sum += i
    if max_sum < current_max_sum:
      max_sum = current_max_sum
    if current_max_sum < 0:
      current_max_sum = 0
  return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-500,900]))
print(maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))
print(maxSubArray([-2, 1, -3, 4]))
print(maxSubArray([-2, -5, 6, -2, -3, 1, 5, -6]))
print(maxSubArray([-2,-1, -3, 4, -1, 2, 1]))
