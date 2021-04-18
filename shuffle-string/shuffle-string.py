class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
            output = [x for x in range(len(s))]
            i = 0
            for letter in s:
                output[indices[i]] = letter
                i += 1
            return ''.join(output)