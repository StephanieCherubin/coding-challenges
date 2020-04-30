# Given an array a of n numbers and a count k,
# find the k largest values in the array.

# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k => [6, 8, 7]

# First Method: sort
def return_largest_values(arr, k):
    # arr.sort() # O(n log n)
    arr.sort(reverse = True)
    
    for num in range(k): 
        return arr[:-(len(arr)-k)]
        
arr=[5, 1, 3, 6, 8, 2, 4, 7]
k=3    

print(return_largest_values(arr, k))


# Second Method: Use a temp list
def return_max_elements(arr, k): 
    final_list = [] 
  
    for i in range(0, k):  
        max1 = 0
          
        for j in range(len(arr)):      
            if arr[j] > max1: 
                max1 = arr[j]; 
                  
        arr.remove(max1); 
        final_list.append(max1) 
          
    print(final_list) 
  
# Driver code 
arr = [2, 6, 41, 85, 0, 3, 7, 6, 10] 
k = 4
  
return_max_elements(arr, k) 