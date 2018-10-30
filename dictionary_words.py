import random, sys

def dictionary_words(arg):
defaultdict = open('/usr/share/dict/words', 'r')

    for word in defaultdict:
        choice = random.randrange(arg)
    return words


    #open the default dictionary
    #take an integer that sets the amount to pick
    #pick random words
    # return random words