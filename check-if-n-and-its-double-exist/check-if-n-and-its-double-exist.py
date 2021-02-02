class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, num in enumerate(arr):
            double = num * 2
            if double in arr:
                j = arr.index(double)
                if i != j:
                    return True
        return False