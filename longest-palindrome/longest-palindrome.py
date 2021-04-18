class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        dict = {}
        for i in s:
            if i not in dict:
              dict[i] = 1
            else:
              dict[i] = dict[i] + 1
          # iterate over dict 
        for key, value in dict.items():
            if value % 2 == 0:
                count += value 
                dict[key] = 0
            elif value % 2 ==1 and value > 1:
                count += value - 1
                dict[key] = 1
      #  second iteration to catch 1 odd value
        for value in dict.values():
            if value > 0:
                return count +1 
        return count