class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        slist= list(S)
        i = 0
        j = len(S) -1
        while i < j:
            if slist[i].isalpha() and slist[j].isalpha():
                slist[i], slist[j] = slist[j], slist[i]
                i += 1
                j -= 1
            elif not slist[i].isalpha():
                i += 1
            elif not slist[j].isalpha():  
                j -= 1 
        return "".join(slist)  