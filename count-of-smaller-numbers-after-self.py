def countSmaller(nums):
    "You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i]."
    
    output = []
    # dict = {}
    # for index, i in enumerate(nums):
    #     count = 0
    #     for jindex, j in enumerate(nums):
    #         if index < jindex and i > j:
    #             print('i:',i, 'j:', j)
    #             count += 1
    #     output.append(count)
    # return output
    for index, i in enumerate(nums):
        count = 0
        while index < len(nums):
            for jindex, j in enumerate(nums):
                if index < jindex and i > j:
                    print('i:',i, 'j:', j)
                    count += 1
        index += 1
        output.append(count)
    return output

            
                
# create an output array
# loop over array
    # if the next number is less than current.
    # add that count number to the output array.





print(countSmaller([5,2,6,1])) 
# Output: [2,1,1,0]
print(countSmaller([5,6,6,1,2])) 
# Output: [1,1,1,0, 0]
{index:count}

