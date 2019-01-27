'''Write a function that takes a string as input
and reverses only the vowels of a string.'''

def reverse_vowels(string_proper):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if ( alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)

for vowel in filteredVowels:
    print(vowel)

'''Given a string, set the variable constant for vowels.
Use a for loop to iterate through the string.
If character is a vowel:
replace with another dummy character,
but remove it from the string.
Use reverse function or slicing to reverse the string.
replace dummy values with vowels.'''