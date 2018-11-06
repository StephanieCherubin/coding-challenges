import random, sys


def dictionary_words(arg):
    defaultdict = open('/usr/share/dict/words', 'r')
    random_words = random.randrange(defaultdict)
        if
    print(random_words)

    #open the default dictionary
    #take an integer that sets the amount to pick
    #pick random words
    # return random words

def rearrange(list):
    random_index = random.randrange(len(list))
    counter = 5
    while counter > 0:
        word_word = list.pop(random_index)
        list.append(word_word)
        counter -= 1
    result = ' '.join(list)
    print(result)


def main(list):
    rearrange(list)


if __name__ == '__main__':
    params = sys.argv[1:]
    main(params)