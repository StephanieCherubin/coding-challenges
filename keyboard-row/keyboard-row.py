class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        output = []
        for word in words:

            if len(set(word.lower())) == len(set(word.lower()).intersection(first_row)):
                output.append(word)
            elif len(set(word.lower())) == len(set(word.lower()).intersection(second_row)):
                output.append(word)
            elif len(set(word.lower())) == len(set(word.lower()).intersection(third_row)):
                output.append(word)
        return output