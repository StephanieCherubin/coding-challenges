'''Write a recursive function that returns the factorial of a given number'''

def factorial(n):
    	
	if n < 2 :
		return 1
	return n * factorial(n-1)
	
def main():
    	print(factorial(5))
if __name__ == "__main__":
	main()