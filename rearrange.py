import sys
import random

myString = "how now brown cow"

def Convert(string):
    myList = list(string.split(" "))
    random.shuffle(myList)
    return myList

if __name__ == '__main__':
    answer = ' '.join(Convert(myString))
    print(answer)

# import random
#
# quotes = ["how"]["now"]["brown"]["cow"]
#
# def random_python_quote():
#     rand_index = random.randint(0, len(quotes) - 1)
#     return quotes[rand_index]
#
# if __name__ == '__main__':
#     quote = random_python_quote()
#     print(quote)