# Replace the string you want to shuffle with myString
import random
import sys

def rearrange(list):
    random_index = random.randrange(0, len(list))
    counter = 5
    while counter > 0:
        word_word = list.pop(random_index)
        list.append(word_word)
        counter -= 1
    print(list)


def main(list):
    rearrange(list)


if __name__ == '__main__':
    # mylist = []

    params = sys.argv[1:]
    main(params)