
def frequency(words):
    frequency_dictionary = {}

    for key in words:
        if key in frequency_dictionary:
            frequency_dictionary[key] += 1
        else:
            frequency_dictionary[key] = 1
    return frequency_dictionary


# for loop to get key.
# Get value to key.
# Take the range in the dictionary and sum them.
# For item in range.
# Iterate 4 times if four.
# Append keys in array
# Make sure the frequency of each list item is accounted for.
# take a random index from list

# open this text file
# FIXME: figure out how to use with open that's self closing
text_file = open("dr-seuss.txt","r")
# read this text file and place items in a list to split
list = text_file.read()
myList = list.split()
total_word_count = len(myList)
print('Total word count: {}'.format(total_word_count))
# use the above function to take frequency and place back in the dictionary
final_dictionary = frequency(myList)
print('Final Dict: {}\n'.format(final_dictionary))
# print(final_dictionary.keys())
print('My List: {}'.format(myList))

text_file.close()



def randomized_item():
    for value in final_dictionary:
        value = final_dictionary[key]
    return value/total_word_count

print(randomized_item())


