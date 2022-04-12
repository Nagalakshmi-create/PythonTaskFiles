#Create a function that determines whether a number is a Disarium or not.

def disarium(n) :
    '''Check whether the given number is disarium or not

            Parameters:
                n (int): any integer
                
             Return:
                Returns 0 or 1 --> '0' means not a disarium number
                                   '1' means disarium number
    '''


    length = len(str(n))      #to find length of number
    sum = 0  
    x = n
    while (x > 0) : 
        remainder = x % 10           # to find last number
        sum += remainder ** (length)
        length = length - 1
        x = x//10                  # to find first numbers by leaving last number  
        
    if sum == n :
        return 1
    else :
        return 0

number = int(input("Enter a number: "))

if (disarium(number) == 1) :
    print ("Disarium Number")
else :
    print ("Not a Disarium Number")
