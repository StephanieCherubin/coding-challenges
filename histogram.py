# Read a file and import it.
# Count number of words in that file.

def frequency(words):
    # create a dictionary to add words into
    frequency_dictionary = {}
    for key in words:
        if key in frequency_dictionary:
            # add 1 to value amount and update value if more than 1
            frequency_dictionary[key] += 1
        frequency_dictionary[key] = 1
    return frequency_dictionary

# open this text file
text_file = open("dr-seuss.txt","r")
# read this text file and place items in a list to split
list = text_file.read()
input = list.split()
# use the above function to take frequency and place back in the dictionary
frequency_dictionary = frequency(input)
print(frequency_dictionary)

# uppercase, lowercase, punctuation
# remove everything else.
# function read filename
# another function to take in a string
# and output histogram