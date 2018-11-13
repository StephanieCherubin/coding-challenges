'''Given a list of integers, find the highest product you can get from three of the integers'''

def biggest_product(ls):
  for x in range(len(ls)):
      for y in range(x + 1, len(ls)):
        if ls[x] > ls[y]:
          ls[x], ls[y] = ls[y], ls[x]

  list_len = len(ls)
  highest_num = 0
  for i in range(list_len):
    current_index = ls[i]
    for j in range(i +1 , list_len):
      if j < (list_len -1):
        product = current_index * ls[j] * ls[j+1]
        if product > highest_num:
          highest_num = product
  return highest_num

print(biggest_product([3, 7, 11, 19, 27]))
print(biggest_product([ 1, 0, 1, 0, 1]))
print(biggest_product([-90, 1]))
print(biggest_product([-9]))
print(biggest_product([64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]))

'''Method 2'''
# from itertools import permutations
# ls = list(permutations(range(1, 4)))
# print(ls)

'''Method 3
Python function to print permutations of a given list'''
 # def permutation(lst):

'''If lst is empty then there are no permutations'''
# if len(lst) == 0:
    #     return []

'''If there is only one element in lst then, only
    one permuatation is possible'''
# if len(lst) == 1:
#     return [lst]

'''Find the permutations for lst if there are
    more than 1 characters'''

# l = []  '''empty list that will store current permutation'''

'''Iterate the input(lst) and calculate the permutation'''
# for i in range(len(lst)):
#    m = lst[i]

'''Extract lst[i] or m from the list.  remLst is
       remaining list'''
   # remLst = lst[:i] + lst[i+1:]

'''Generating all permutations where m is first
        element'''
#    for p in permutation(remLst):
#        l.append([m] + p)
# return l


'''Driver program to test above function'''
# data = list('123')
# for p in permutation(data):
#     print(p)

