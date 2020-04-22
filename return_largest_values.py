# Given an array a of n numbers and a count k find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]

def return_largest_values(arr, k):
    # arr.sort() # O(n log n)
   
    arr.sort(reverse = True)
    
    for num in arr: 
        return arr[:-(len(arr)-k)]
        
arr=[5, 1, 3, 6, 8, 2, 4, 7]
k=3    

print(return_largest_values(arr, k))

  