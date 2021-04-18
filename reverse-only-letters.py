def reverseOnlyLetters(s):
    """Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions."""
    
    # Create a variable to hold the new string.
    # Convert into a list
    
    # Loop over each character in the input string. (While loop (while i is <J))
        # If character is alpha, 
            # swap
        # Else:
            #continue
    slist= list(s)
    i = 0
    j = len(s) -1
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
    
    
    
# print(reverseOnlyLetters("ab-cd")) # Output: "dc-ba"
# print(reverseOnlyLetters("a-bC-dEf-ghIj")) # Output: "j-Ih-gfE-dCba
print(reverseOnlyLetters("Test1ng-Leet=code-Q!")) #Output: "Qedo1ct-eeLg=ntse-T!"Qedo1ct-eeLg=ntse-T!