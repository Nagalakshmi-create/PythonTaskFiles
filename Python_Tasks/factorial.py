#Create a function that takes an integer n and returns the factorial of factorials ..do it using recursive function

def factorial(n):

    '''
        returns multiplication of our number with factorial of (number-1)
    '''
    if n == 0:             # base case
        return 1
     
    return n * factorial(n-1)        #recursive function

def factoffact(n):
    fact=1

    while n !=0:
        fact = factorial(n) *fact
        n -=1
        
    return fact

n = int(input("Enter a number: "))
print(factoffact(n))