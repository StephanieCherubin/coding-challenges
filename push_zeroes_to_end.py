# Python3 code to move all zeroes at the end of array

# Function that pushes all zeroes to end of an array
def pushZeroesToEnd(arr, n):
	count = 0 # Count of non-zero elements

	#Traverse the array. If element encountered is non-zero, then replace the element at index 'count' with this element
	for num in range(len(arr)):
		if arr[num] != 0:
    			
    		# here count is incremented
			arr[count] = arr[num]
			count += 1
					
	# Now all non-zero elements have been shifted to front and 'count is set as index of first 0. Make all elements 0 from count to end
	while count < len(arr):
		arr[count] = 0
		count += 1

if __name__ == "__main__":
	arr = [1, 1, 3, 4, 24, 0, 10, 2, -7, 47, 6, 0, 9]
	pushZeroesToEnd(arr, len(arr))
	print(f'Array after pushing all zeros to end of array: {arr}')
			


