# Python3 code to move all zeroes at the end of array

# Function that pushes all zeroes to end of an array
def pushZeroesToEnd(arr, n):
	count = 0 # Count of non-zero elements

	#Traverse the array. If element encountered is non-zero, then replace the element at index 'count' with this element
	for num in range(len(arr)):
		if arr[num] != 0:
			arr[count] = arr[num]
			count += 1
					
	while count < len(arr):
		arr[count] = 0
		count += 1

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZeroesToEnd(arr, n)
print(f'Array after pushing all zeros to end of array: {arr}')
			


