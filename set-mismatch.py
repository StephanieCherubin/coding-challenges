from collections import Counter

def findErrorNums(nums):
    # '''You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
    # You are given an integer array nums representing the data status of this set after the error.
    # Find the number that occurs twice and the number that is missing and return them in the form of an array.'''
    
    nums = sorted(nums)
    numerical = list(range(1, max(nums)+1))

    print('numerical:', numerical)
    print('nums:', nums)
    # output = []
    # for i in numerical:
    #     if i not in nums:
    #         output.append(i)
    # print(output)
    
              
            
    
# print(findErrorNums(nums = [1,2,2,4])) # Output: [2,3]
# print(findErrorNums(nums = [1,1])) # Output: [1,2]
# print(findErrorNums(nums = [3,2,2])) # Output: [2,1]
print(findErrorNums(nums = [3,2,3,4,6,5])) # Output: [3,1]