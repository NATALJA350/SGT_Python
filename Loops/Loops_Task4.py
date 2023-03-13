#Task 4. Create calculator:
#   Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). If the operation 
#   provided does not match one of these, the program should print 
#   "Operation provided isn't valid, please,try again" - in this case, the program should
#   ask for the operation to be provided again

# while True:
#     # operation = input("Add","Substract","Myltiply","Divide")
#     operation = input("+")
#     numOne = int(input("Enter first number: "))
#     numTwo = int(input("Enter second number: "))

#     if operation == "+":
#         sum = NumOne + numTwo
#         print("The sum is:", sum)
#     else:
#        print("Operation provided isn't valid, please,try again")

# numOne = int(input("Enter the first number: "))
# numTwo = int(input("Enter the second number: "))
# operation = input("Enter the operation from the list (*, /, +, -, %)")

# result = 0
# if operation == "*":
#     result = numOne*numTwo
# elif operation == "/":
#     result = numOne/numTwo
# elif operation == "+":
#     result = numOne+numTwo
# elif operation == "-":
#     result = numOne-numTwo
# elif operation == "%":
#     result = numOne%numTwo
# else:
#     print("Operation provided isn't valid, please,try again")
#     print("your answer is: ", result)

# numOne = int(input("Enter the first number: "))
# operation = input("Enter the operation from the list (*, /, +, -, %)")
# numTwo = int(input("Enter the second number: "))

# result = 0
# if operation == "*":
#     result = numOne*numTwo
# elif operation == "/":
#     result = numOne/numTwo
# elif operation == "+":
#     result = numOne+numTwo
# elif operation == "-":
#     result = numOne-numTwo
# elif operation == "%":
#     result = numOne%numTwo
# else:
#     print("Operation provided isn't valid, please,try again")
#     print("your answer is: ", result)

while True:
  
    operation = input("Enter the operation from the list (*, /, +, -, %)")
    if operation != "*" and operation != "/" and operation != "+" and operation != "-" and operation != "-" and operation != "%":
        print("Operation provided isn't valid, please,try again")
        continue

    numOne = int(input("Enter the first number: "))
    numTwo = int(input("Enter the second number: "))

    if operation == "*":
        print(numOne * numTwo) 
    elif operation == "/":
        print(numOne / numTwo) 
    elif operation == "+":
        print(numOne + numTwo) 
    elif operation == "-":
        print(numOne - numTwo) 
    elif operation == "%":
        print(numOne % numTwo) 
  