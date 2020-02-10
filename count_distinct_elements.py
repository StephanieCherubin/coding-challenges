#something about counting the number of unique numbers {1:1} {2:3} {3:4}

 # Python program to count the frequency of  
# elements in a list using a dictionary 
def countDistinctElements(my_list):
    count = 0 
    
    # create an empty dictionary
    values_dictionary = {}
    for element in my_list:
        if element not in values_dictionary:
            values_dictionary[element] = 1
        else:
            values_dictionary[element] += 1

    for key, value in values_dictionary.items():
        # print ("% d : % d"%(key, value)) 
        if value > 1:
            print(f"The number {key} occurs {value} time(s).")
            count +=1
    print(f"Total distinct element count is: {count}") 

if __name__ == "__main__":
    my_list = [1,2,3,2,3,3,44,4,4,3,2]
    countDistinctElements(my_list)