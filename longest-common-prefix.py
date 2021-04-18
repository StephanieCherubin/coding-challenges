def longestCommonPrefix(strs):
    '''Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".'''
    common_letters = ''
    for i in range(len(strs[0])):
        for j in range(len(strs[1])):
            if strs[i] == strs[j]:
                return 'hell yes'
    return 'yes'
    
            
print(longestCommonPrefix(["flower","flow","flight"])) #"fl"
# b = longestCommonPrefix(["dog","racecar","car"]) #""
# print(b)
# c = longestCommonPrefix(["nyalief","nyapal","nyatit", "nyakuoth"]) #"nya"
# print(c)    