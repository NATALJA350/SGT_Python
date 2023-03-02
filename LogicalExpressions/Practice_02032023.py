
# Task 1. 
# Create a program that asks the user to enter their age and whether or not they have a driver's license. 
# If the user is at least 18 years old and has a driver's license, the output should be as follows
# "You are able to drive : True
# If not, then
# "You are able to drive : False

userAge = int(input ("Please enter your age: "))
print(userAge)
userDriverLic = str(input ("Do you have a driver license? Yes or No: ")) 
print(userDriverLic)

if userAge >= 18 and userDriverLic == str("Yes"):
    print("You are able to drive.")

else:
    print("You are NOT able to drive.")


# Task 2. (Explore some String functions).Create a program that asks the user for a password, and checks if it meets the following criteria: at least 8 characters long
# If the password meets all of these criteria, print "Password accepted : True", otherwise print "Password accepted : False".

password = str(input("Enter the password 8 characters long: "))
if len(password) >= 8:
    print("Password accepted : True")
else: 
    print("Password accepted : False")

# Task 3. Write a program that asks the user to enter two integers and checks if they are both even. 
# If they are, print "Both numbers are even : True", otherwise print "Both numbers are even : False".
# If at least one is even print "At least one number is even : True", else "At least one number is even : False".

numOne = int(input("Please enter Number One: "))
numTwo = int(input("Please enter Number Two: "))

if numOne % 2 == 0 and numTwo % 2 == 0:
    print("Both numbers are even : True") # both numbers are even
elif (numOne + numTwo) % 2 == 1:
    print("At least one number is even : True") #one number is even, other is odd
else:   
    print("At least one number is even : False") # both numbers are odd


# Task 4. Write a program that asks the user to enter a year and checks if it is a leap year. 
# A leap year is defined as a year that is divisible by 4 but not by 100, or a year that is divisible by 400. 
# If the year is a leap year, print "Leap year : True", otherwise print "Leap year : False".

year = int(input ("Please enter a year: "))
if (year % 4 == 0) and (year  % 100 != 0) or (year % 400 == 0):
    print("Leap year : True")
else:
    print("Leap year : False")

#Task 5. Create the program which asks to enter the date (day, month, year). 
# If the date is valid print : "Date valid : True" else "Date valid : False

import datetime 
date = input("Enter the date in format DD/MM/YYYY")
day, month, year = date.split("/")
dateValid = True
try:
    # datetime.datetime(int(day), int(month), int(year))
    datetime.datetime(int(year), int(month), int(day))
except:
    dateValid = False
if(dateValid):
        print("Date valid : True")
else:
    print("Date valid : False")
