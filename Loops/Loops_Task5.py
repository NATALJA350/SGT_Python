#Task 5. Write a program that takes an integer as input and prints out whether that integer is prime or not.

# num = int(input("Enter number: "))
# if num >= 1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             print(num," is not a prime number")
#             break
        
#     else:
#         print(num," is a prime number")
# else:
#     print(num," is not a prime number")


num = int(input("Enter number: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num," is a prime number")
            break
        
    else:
        print(num," is not a prime number")
            
else:
    print(num," is a not a prime number")
    