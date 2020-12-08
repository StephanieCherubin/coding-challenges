class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for n in nums:
            output.append(n**2)
        output.sort()
        return output
