<<<<<<< HEAD
def arrayStringsAreEqual(word1, word2):
    "Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise. A string is represented by an array if the array elements concatenated in order forms the string."
    
    # concatenate all strings for word1
    word1_concat = "".join(word1)
    
    # concatenate all strings for word2
    word2_concat = "".join(word2)
  
    #  if word1 == word2:
    if word1_concat == word2_concat:
        return True
    else:
        return False
        # return true
    # else return false
print(arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
# Output: true
print(arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
# Output: false
print(arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))
# Output: true  
=======
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_concat = "".join(word1)
    
        word2_concat = "".join(word2)
​
        if word1_concat == word2_concat:
            return True
        else:
            return False
>>>>>>> 5d0a94d9777893ecfe1daa85b0e94fa43af7a519
