# Replace the string you want to shuffle with myString
import random


myString = "how now brown cow"

def convert(string):
    myList = list(string.split())
    random.randrange(len(myList))
    return myList

if __name__ == '__main__':
    print(' '.join(convert(myString)))
    # print(rearrange)