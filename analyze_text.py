# I created a program that analyzes text from a user
# and returns the number of e's in the text as well as the percentage.
# I wanted to use a common letter, and the letter e is the most common letter
# in the English alphabet.

def analyze_text(text):
    total_e = 0
    totalletters = 0
    for i in range(len(text)):
        if text[i].isalpha()==True:
            totalletters = totalletters +1
        if text[i] == "e" or text[i] == "E":
            total_e = total_e + 1
    percent = total_e/totalletters*100
    return "The text contains " + str(totalletters)+ " alphabetic characters, of which " + str(total_e)+ " ("+ str(percent) + "%) are 'e'."