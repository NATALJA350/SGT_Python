#Task 3. Write a program that takes an integer as input and prints out all the factors of that integer.

# #using for loop
# num = int(input("Enter number: ")) #take int as input
# print("The factors of this numbers are : ") # find and print out all factors of int numbers
# for i in range(1, num+1):
#     if(num % i) == 0:
#         print (i, end=" ")

#using while loop
num = int(input("Enter number: ")) #take int as input

print("The factors of", num, "are: ") # find and print put all factors of int numbers
i = 1
while(i <= num):
    if(num % i == 0):
        print(i, end=" ")
    i = i+1
        
