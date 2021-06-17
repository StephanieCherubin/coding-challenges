class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if i in s_dict and s_dict[i] >0:
                s_dict[i] -= 1  

        return sum(s_dict.values())