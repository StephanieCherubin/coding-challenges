class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while end > start:
            summ = numbers[start] + numbers[end]
            if (summ == target):
                return [start + 1, end + 1]
            if (summ > target):
                end -= 1
            elif (summ < target):
                start += 1