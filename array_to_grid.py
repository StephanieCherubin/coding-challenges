# Given an array of values you need to map the values on to a grid. Return an array of objects containing the original value, and a row and col that would represent the position of where the object would map on the grid. Assume the length of the original array is always a square e.g. 4, 9, 16 etc. Assume the grid has an equal height and width.

# Sample input

array =[1,2,1,1,
 1,2,2,1,
 1,2,3,0,
 1,1,1,0]

#Square root the number of items in array.
#Result would be length- height of array
import math

def grid(array):
    length = len(array)
    
    array_width = int(math.sqrt(length))
    final_grid = []
    for item in range(0, length, array_width):
        subarray = array[ item:item + array_width ]
        final_grid.append(subarray)
    
    return  final_grid
    
print(grid(array))

