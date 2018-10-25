import sys
import random

def Convert(string):
    myList = list(string.split(" "))
    random.shuffle(myList)
    return myList

myString = "how now brown cow"

answer = ' '.join(Convert(myString))
print(answer)