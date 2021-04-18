def checkIfExist(arr):
    '''Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).'''
    for num in arr:
        double = num * 2
        if double in arr:
            return True
        return False
    
print(checkIfExist(arr = [10,2,5,3])) # true
print(checkIfExist(arr = [7,1,14,11])) #true
print(checkIfExist(arr = [3,1,7,11])) #false
