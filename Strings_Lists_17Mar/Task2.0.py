#Task2
#Write the program to sort the list (without using sort function). You can implement any algorithm

list = [1, 17, 0, -2, -42, 67]
num = len(list)

for i in range(num):
    for j in range(i+1, num):
        if list[i] > list[j]:
            list[i], list[j] =  list[j], list[i]

print(list)

# list = [1, 17, 0, -2, -42, 67]
# newList = []

# for i in range(len(list)):
#    j = min(list)
#    newList.append(j)
#    list.remove(j)

# print(newList)