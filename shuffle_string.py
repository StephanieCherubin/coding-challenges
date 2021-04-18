def restoreString(s, indices):
    '''Given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.'''

    #Create an array to hold characters
    # Iterate over letters in string (for loop)
        # Add index to each character
    output = [x for x in range(len(s))]
    i = 0
    for letter in s:
        output[indices[i]] = letter
        i += 1
    return ''.join(output)
    # return output string
print(restoreString("art", [1,0,2])) # "rat"
print(restoreString("codeleet", [4,5,6,7,0,2,1,3])) #"leetcode"
print(restoreString("aaiougrt", [4,0,2,6,7,3,1,5])) #"arigatou"


