# import sys

# def dictionary_words(arg):
#     for word in open('/usr/share/dict/words'):


# if __name__ == '__main__':
defaultdict = open('/usr/share/dict/words')
words = defaultdict(list)
with open('/usr/share/dict/words') as fin:
    for word in fin:
        if len(word) == 5:
            words.append(word)

for letter in ascii_lowercase:
    print (letter, 'is for', choice(words[letter]))
