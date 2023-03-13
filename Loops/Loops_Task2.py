#Task2. Write a program that prints out the numbers from 1 to 100. 
#But for multiples of three, print "Fizz" instead of the number 
#and for multiples of five, print "Buzz". 
#For numbers that are multiples of both three and five, print "FizzBuzz".

for i in range(1,101):

    if (i % 15) == 0: #are multiples of both three and five
        print(i, "| FizzBuzz")
    
    elif (i % 3) == 0: #are multiples of three
        print(i, "| Fizz")  
    
    elif (i % 5) == 0: #are multiples of five
        print(i,"| Buzz")

    else:
        print(i, "| ", i)

# for i in range(1,101):
    
#     if (i % 3) == 0: #are multiples of three
#         print(i, "Fizz")  
    
#     elif (i % 5) == 0: #are multiples of five
#         print(i,"Buzz")

#     elif (i % 3  and ) == 0: #are multiples of both three and five
#         print(i,"FizzBuzz")

#     else:
#         print(i)