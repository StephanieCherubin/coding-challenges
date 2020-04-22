def findPairs(arr1, arr2, t): 
  '''find all pairs in both arrays whose  
  sum is equal to given value  '''
  
  for i in range(0, len(arr1) ): 
      for j in range(0, len(arr2) ): 
          if (arr1[i] + arr2[j] == t): 
              print([arr1[i], arr2[j]])

findPairs(arr1 = [9, 13, 1, 8, 12, 4, 0, 5]  , arr2 = [0, 7, 4, 3, 2, 1] , t= 13)
  
  
  
  
  
  
  
  
  
  
  
  # Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20 ⇒ [13, 6] or [4, 17] or [5, 14]

def complex_two_sum(a, b, t):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    
    start_a = 0
    end_b = len(b) -1
  
    while start_a <= end_b:
        sum_pair = sorted_a[start_a] + sorted_b[end_b]
        
        if sum_pair == t:
            return [sorted_a[start_a], sorted_b[end_b]]
        if sum_pair  < t:
            start_a += 1
        if  sum_pair  > t:
            end_b -= 1
        # Solve the off by one error:
        #  if (sum_pair[0] - sum_pair[1])  - sorted_a[start_a] + sorted_b[end_b]:
            
    return [sorted_a[start_a], sorted_b[end_b]]

b=[3, 4, 6, 14, 17]
a = [0, 1, 4, 5, 8,9, 12,13]
t = 20
print(complex_two_sum(a, b, t))