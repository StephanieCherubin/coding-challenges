class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0: #even
                num = num / 2
                step +=1
            else: #odd
                num = num - 1
                step +=1
        return step