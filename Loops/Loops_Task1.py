#Task 1. Write a program that takes a user input (an integer) and determines whether it is positive, negative, or zero.

num = int(input("Enter number: "))
if num > 0:
        print(num," is positive")
elif num == 0:
        print(num," is zero")
else: 
    print(num," is negative")
