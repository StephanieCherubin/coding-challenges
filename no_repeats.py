'''Given a string, find the first non-repeating character
in it and return its index. If it doesn't exist, return -1.'''

myList = ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"]
def frequency(words):
    frequency_dictionary = {}

    for key in words:
        if key in frequency_dictionary:
            frequency_dictionary[key] += 1
        else:
            frequency_dictionary[key] = 1
    return frequency_dictionary


final_dictionary = frequency(myList)
print(final_dictionary.values())
if final_dictionary.values() == 1:
    print(final_dictionary.keys())
else:
    print(-1)
