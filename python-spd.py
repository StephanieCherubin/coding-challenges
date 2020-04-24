def findT(arr, t):
  for num in arr:
    i = 1
    sum = arr[num] + arr[num + i]
    if sum == t:  
      return (arr[num], arr[num + i])
    else:
      i += 1

print(findT([11, 7, 3, 9, 17], 16))