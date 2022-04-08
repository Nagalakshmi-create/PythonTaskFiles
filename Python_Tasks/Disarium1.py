#Create a function that determines whether a number is a Disarium or not.

def disarium(n):  #178

    num_list = list(n)   #['1', '7', '8']
    length = len(num_list)   #3
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