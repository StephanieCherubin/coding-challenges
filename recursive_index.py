'''Given a sorted array of strings, write a recursive function to find the index of the first and last occurrence of a target string. If the target string is not found in the array, report that.
Example input:  instructors = [Adriana, Adriana, Alan, Alan, Alan, Alan, Alan, Braus, Braus, Braus, Braus, Dan, Dan, Dan, Dan, Dan, Dani, Dani, Jess, Meredith, Milad, Milad, Mitchell, Mitchell, Mitchell, Mitchell]
Example execution:  find_indexes(instructors, 'Braus')  => (7, 10)'''

def recursive_index(arr, target, index = 0):
    list1 = [None, None]
    
    # if target in array,
    # starting index will be first value
        # for last value, if next value is different:
            # return the value before the different
    if target == arr[index]:
        list1[0] = index
        list
        
        
        return recursive_index(arr, target, index + 1)
    return list1
    
def findFirstAndLast(arr, n, target) : 
    first = -1
    last = -1
    for i in range(0,n) : 
        if (target != arr[i]) : 
            continue
        if (first == -1) : 
            first = i 
        last = i 
      
    if (first != -1) : 
        print( "First Occurrence = " , first,  
               " \nLast Occurrence = " , last) 
    else : 
        print("Not Found") 
instructors = ['Adriana', 'Adriana', 'Alan', 'Alan', 'Alan', 'Alan', 'Alan', 'Braus', 'Braus', 'Braus', 'Braus', 'Dan', 'Dan', 'Dan', 'Dan', 'Dan', 'Dani', 'Dani', 'Jess', 'Meredith', 'Milad', 'Milad', 'Mitchell', 'Mitchell', 'Mitchell', 'Mitchell']
     
print(findFirstAndLast(instructors, len(instructors), 'Braus'))