
def maxSubArray(nums):

  current_max_sum = 0
  max_sum = 0

  for i in nums:
    if len(nums) == 1:
          return nums
    current_max_sum += i
    if max_sum < current_max_sum:
      max_sum = current_max_sum
    elif current_max_sum < 0:
      current_max_sum = 0
  return max_sum

if __name__ == '__main__':
  print(maxSubArray([-1]))
  # print(maxSubArray([-2,1,-3,4,-1,2,1,-500,900]))
  # print(maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3]))
  # print(maxSubArray([-2, 1, -3, 4]))
  # print(maxSubArray([-2, -5, 6, -2, -3, 1, 5, -6]))
  # print(maxSubArray([-2,-1, -3, 4, -1, 2, 1]))
