'''Write a function that returns true/false if a given string is a palindrome or not'''

#input race-car
#output true

def palindrome(text):

    clean = text.replace("-", "")
    clean = clean.replace("_", "")
    
    return clean == clean[::-1]
        
print(palindrome('race_car')) #true
print(palindrome('taco-_cat'))#true
print(palindrome('rocket ship')) #false