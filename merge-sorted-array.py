def merge(nums1, m, nums2, n):
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    """
    
    # Loop through nums1:
    
    # if any zeros exist, delete them
    
    # nums2 = nums1 + nums2

# newlist = [expression for item in iterable if condition == True]

    for i in range(len(nums1)):
        if nums1[i] == 0:
            nums1[i] = nums2[0] #list index out of range
            del nums2[0]
    nums1.sort()
    return nums1

# print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)) 
print(merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [2,5,6], n = 3))

# Output: [1,2,2,3,5,6] 





    