# Given an array of a of n numbers and a target value t, find two numbers whose sum is t.
# Example a =[5,3,6,8,2,4,7], t=10 => [3,7] or [6,4] or [8,2]

# First way:
    # Take the first number in array a and sum it against the second number.
        # if the two numbers add up to the target value t, stop.
        # return the two numbers that added to t
    # Then sum the 1st number against the third number
        # Repeat the if block.
    # Do this until you reach the end of the list.
    
   # O(n)
   
# Second Way:
    # Sort the array from highest to lowest
    # Start with the two numbers in the direct middle of the array.
        # If there are 3 numbers in the direct middle, choose the lower two.
    # With the two numbers, and them up to see if they get to the target t.
        # if the result is the target, return the two numbers.
        # if the result is lower than the target, move the numbers summed to the right.
        # if the result is higher than the target, move the numbers summed to the right.
            # return the first two numbers that add up to the target.

# Third Way
