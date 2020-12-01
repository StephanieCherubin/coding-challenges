"""Assignment 2
Code out 2 solutions. Use your pseudocode to guide your comments.
Twitter Follow Suggestions
You’re working an internship at Twitter and are tasked to improve suggestions for accounts to follow, which already works great for established accounts because it uses content from your tweets and other accounts you follow to suggest new ones. However, when a new user signs up none of this information exists yet, but Twitter still wants to make some follow suggestions. Your team asked you to implement a function that accepts a new user’s handle and an array of many other users’ handles, which could be very long – Twitter has over 330 million active accounts! You need to calculate a similarity score between a pair of handles by looking at the letters each contains, scoring +1 for each letter in the alphabet that occurs in both handles but scoring –1 for each letter that occurs in only one handle. Your function should return k handles from the array that have the highest similarity score to the new user’s handle.

Example execution:
handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']

TIPS:
Use the simplifications that were brainstormed in class.
Create a plan for how you’ll solve the problem from the absolute simplest possible version as step 1, then remove one of the simplifications in step 2, then another in step 3, and finally remove all simplifications so you are solving the full version of the problem in your final step. DO NOT attempt to solve the full version of the problem right away. The goal of this is to break the problem down into smaller, simpler steps to create an incremental path from the simplest version to the full problem. Practicing this will help you during real interviews, especially when you hear a new problem and think to yourself “OMG this is hard!” – This is to develop a strategy for how to move past those thoughts.

"""

# handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
# my_handle = 'iLoveDogs'
# suggest('iLoveDogs', handles, k=2)   should return   ['GodIsLove', 'DogeCoin']
number_of_suggestions = 1


# helper function for similarity score between 2 handles
# solve problem with number of suggestion = 1

def suggest(handles, my_handle, k):
    # to access each letter
    pass


    

def frequency(handle):
    # freq_dict = { }
    
    # for letter in handle:
    #     if letter in freq_dict:
    #         freq_dict[letter] += 1
    #     else:
    #         freq_dict[letter] = 1
                      
    # return freq_dict
    
print(frequency('DogeCoin'))

def similarity_score(handle, my_handle):
    # increase score based on similar letter
    score = 0
    handle.lower()
    my_handle.lower()
    
    handle = set(handle.split(''))
    my_handle = set(my_handle.split(''))
    
    # find difference of the two sets.
        # difference_set = handle.symmetric_difference(my_handle)
    # find intersection of the two sets
        # instsection_set = handle.intersection()
    # find length of difference set and intersection set
    return score

print(similarity_score('DogeCoin',  'iLoveDogs'))

















    # #convert handle to dictionary
    # handle_dict = frequency(handle) 
    # # loop over characters in my_handle to compare freq dictionary
    # for letter in my_handle:
    #     # if character are in freq_dict
    #     if letter in handle_dict:
    #         # increase score +=1
    #         score += 1
    #     # else:
    #     else:
    #         #decrease score -=1
    #         score -= 1
    # #return similarity score