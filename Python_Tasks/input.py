# 1. create a python module, add function for addition, subtraction, multiplication and division separately in one file
# 2. second file will import any function from above 
# 3. give user input to choose function as well as to giving values for math operations until user says stop

from calculator import *

x = True

while x:
      num1 = int(input("Enter First Number: "))
      num2 = int(input("Enter Second Number: "))

      print("Enter which operation would you like to perform?")
      operators = ['+' , '-' , '*' , '/']
      operation = input("Enter any of these character for specific operation +,-,*,/: ")

      while operation not in operators:            
            operation=input("Enter a valid operator:  ")
      if operation in operators :
            if operation == "+":
                  result = add(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))
            elif operation == "-":
                  result = sub(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))
            elif operation == "*":
                  result = mul(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))
            elif operation == "/":
                  result = div(num1, num2)
                  print(str(num1) + str(operation) + str(num2) + " = " + str(result))

      a = input()
      if a == "stop":
            x = False