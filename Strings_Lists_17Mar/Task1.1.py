#Task1.1
#Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 
#Based on the task 1, count the occurrences of each character in the text provided and display them in the output

text = "Ask the user to enter the text and a letter. Count how many occurrences of the letter provided."

chars = {}
for i in text:
    if i in chars: 
        chars[i] += 1
    else:
        chars[i] = 1
print("Count the occurrences of characters:", chars)




