def good_num(num):
    # Create a dictionary. 
    # Check if num has rotated value.
    # If value is not null return true
    rotated_dict = {0:0, 1:1, 2:5, 3:None, 4:None, 5:2, 6:9, 7:None, 8:8, 9:6}
    if rotated_dict[num] == None:
        return False
    else:
        rotated_dict[num]
    
print(good_num(2)) # True
print(good_num(0)) # False

def rotatedDigits(num):
    "X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone. A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid. Now given a positive number N, how many numbers X from 1 to N are good?"
    # Check each number in range 1 through num
    count = 0
    
    ranges = [x for x in range(1,num)]
    rotated = []
    
    for num in ranges:
        rotated.append(good_num(num))
    
    for i in range(len(range)):
        if
print(rotatedDigits(10))