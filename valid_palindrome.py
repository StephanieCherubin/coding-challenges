import sys

def isPalindrome(self, s):
    s = filter(str.isalnum, str(s)).lower()
    return s == s[::-1]

def main():
  
  args = sys.argv[1:]  # Ignore script file name
  if len(args) > 0:
      for arg in args:
          is_pal = is_palindrome(arg)
          result = 'PASS' if is_pal else 'FAIL'
          is_str = 'is' if is_pal else 'is not'
          print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
  else:
      print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
      print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    
def palindrome(string):
    from re import sub
    s = sub('[\W_]', '', string.lower())
    return s == s[::-1]

palindrome('taco cat') # True
