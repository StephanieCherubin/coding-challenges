class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        stack = []
        vowels = "AaEeEiIoOuU"
        for letter in s: 
            if letter in vowels:
                stack.append(letter)
        for i in range(len(s)):
            if s[i] in vowels:
          #s[index] = item
                s[i] = stack.pop()
        return ''.join(s)