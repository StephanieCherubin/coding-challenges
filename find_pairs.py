def findPairs(arr1, arr2, t): 
  '''find all pairs in both arrays whose  
  sum is equal to given value  '''
  
  for i in range(0, len(arr1) ): 
      for j in range(0, len(arr2) ): 
          if (arr1[i] + arr2[j] == t): 
              print(arr1[i], arr2[j])

findPairs(arr1 = [1, 2, 3, 7, 5, 4]  , arr2 = [0, 7, 4, 3, 2, 1] , t= 13)
  