class Solution:
    def frequencySort(self, s: str) -> str:
        output = ""
        freq = {}
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+= 1

        sorted_freq = sorted(freq.items(), key = lambda x: x[1], reverse = True)

        for item in sorted_freq:
            output += (item[0] * item[1])

        return output