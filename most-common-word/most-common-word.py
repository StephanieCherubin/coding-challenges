class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z\s]', ' ', paragraph.lower())
        for letter in paragraph:
            if letter == ',':
                paragraph = paragraph.replace(letter, ' ')
        str_lst = paragraph.split()

        dic = {}
        for word in str_lst:
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                elif word in dic:
                    dic[word] += 1

        return max(dic, key = dic.get)