#Create a function that determines whether a number is a Disarium or not.

def disarium(n): 
    
    '''returns whether the given number is disarium not
        
        parameters:
            n (int): integer
     '''
    
    num_list = list(n)   
    length = len(num_list)   
    sum = 0

    for i in range(length):
        sum += int(num_list[i]) ** (i+1)
    sum = str(sum)

    if sum == n :
        print ("Disarium Number")
    else :
        print ("Not a Disarium Number")

number = input("Enter a number: ")

disarium(number)
