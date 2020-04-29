'''Write a function that returns true/false if a given string is a palindrome or not'''

#input race-car
#output true


# First Method:
def is_palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]

print(is_palindrome('taco cat')) # True
print(is_palindrome('race_car')) # True
print(is_palindrome('Taco-_Cat'))# True
print(is_palindrome('rocket ship')) # False

# Second Method:
def palindrome(text):
    text = filter(str.isalnum, str(text)).lower()
    clean = text.replace("-", "")
    clean = clean.replace("_", "")
    
    return clean == clean[::-1]

def main():
    print(palindrome('race_car')) #true
    print(palindrome('Taco-_Cat'))#true
    print(palindrome('rocket ship')) #false
    
if __name__ == "__main__":
    main()