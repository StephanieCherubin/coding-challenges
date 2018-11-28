''' '''


# with open("anna_karenina.txt", "r") as f:
#     for k in f:
# replacing = "she"
# def replacement():
#     with open("anna_karenina.txt", "r") as f:
#         for word in f:
#             result = replacing.replace("Oblonskiy", "Oblonskiy")
#             print(result)
# replacement()
import re

filename = 'anna_karenina.txt'

# with open("anna_karenina.txt, "r") as fil
file = open(filename, 'rt')
text = file.read()
file.close()

words = re.sub(r'\W*[^\'\w+\']', " ", text)
print(words)