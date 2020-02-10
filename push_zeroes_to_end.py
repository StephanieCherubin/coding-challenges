# Python3 code to move all zeroes at the end of array

# Function that pushes all zeroes to end of an array
def pushZeroesToEnd(arr):
	for num in arr:
		if num == 0:
			arr.remove(num)
			arr.append(num)

if __name__ == "__main__":
	arr = [0, 1, 1, 3, 4, 24, 0, 0, 0, 10, 2, -7, 47, 6, 0, 9]
	pushZeroesToEnd(arr)
	print(f'Array after pushing all zeros to end of array: {arr}')
			


