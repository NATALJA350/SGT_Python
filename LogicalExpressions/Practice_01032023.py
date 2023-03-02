# a = True
# b = False

# print(a
# print (b)

# a = 23
# b = 10
# c = a * b # c = multiply(a,b)
# print(c) #Result 230

# a = "Hello"
# b = "World"
# c = a + " " + b # c = cocatenate(a,b)
# print(c) # Result Hello World

# a = True
# b = False
# c = a and b  # c = and)a,b) ---> if a is True AND b is True --->>> True, otherwise False
# print(c) #Result False

# a = True
# b = False
# d = False
# c = a and b and c # c = and)a,b) ---> if all  a,b,d are True --> True, otherwise False
# print(c) #Result False

# a = True
# b = False
# d = False
# c = True and True and True # c = and)a,b) ---> if all  a,b,d are True --> True, otherwise False
# print(c) #Result True

# a = True
# b = False
# c = True
# d = True 
# result = a and (b and (c and d))
# print(result) #Result False

# a = True
# b = False
# c = True
# d = True 
# res1 = c and d
# res2 = b and res1
# result = a and res2
# print(result) #Result False

# a = True
# b = False
# c = a or b # or(a,b) ---> True if a OR b is True, otherwise False
# print (c) #Result True

# a = False
# b = False
# c = False
# result = a or b or c
# print (result) # Result False

# a = False
# b = True
# c = False
# result = a or b or c
# print (result) # Result True

# a = True
# b = True
# c = True
# result = a or b or c
# print (result) # Result True

# a = True
# b = True
# c = True
# result = a or b or c
# print (result) # Result True

# # or(and(a,c), b)
# a = True
# b = False
# c = True
# d = False
# result = (a and b) or (c or d) # -->> False or True --> True
# print (result) # Result True

# # or(and(a,c), b)
# a = True
# b = False
# c = True
# d = False
# result = (a and b) + (c or d) # -->> False or True --> True
# print (result) # Result 1

#De Morgan`slaws
# boolean values var1, var2, ..., vrn
# not(var1 or var2 or... varn) = (not var1) and (not var3).. and (not varn)

# a = True
# b = True 
# c = False

# # Same results 
# # result = not (a or b or c)
# # result = not a and not b and not c 
# # print (result) # Result False 

# # Same results (De Morgan`s Law)
# result = not (a and b and c)
# result = not a or not b or not c
# print (result) # Result True 

# a = 20
# b = 10
# c = (a < b) # less(a,b) -->> True if a is less than b, otherwise is False
# print(c) #Result False

# c = a <=b
# #is a < b same as not (a > b)? --> no because we may have the case when a == b
# print(c)

# c = a <= b same as not (a >=b)? --> no because we may have the case when a == b 

# a = 20 
# b = 20 
# c = a == b
# print(c) # Result True

# a = 20 
# b = 21 
# c = (a != b) 
# print(c) # Result True -->> a not equal b


# #example
# astr,bstr,cstr = input("Please, enter values a b c").split()

# a = int(astr)
# b = int(bstr)
# c = int(cstr)

# result = a > b and b < c and a > c
# print("Sequence : b c a : " + str(result))

# result = a > b and b < c and a < c
# print("Sequence : b a c : " + str(result))

# result = a > b and b > c 
# print("Sequence : c b a : " + str(result))

# result = a < b and b > c and a > c
# print("Sequence : c a b : " + str(result))

# result = a < b and b > c and a > c
# print("Sequence : c a b : " + str(result))


a = "Today"
b = "Tomorrow"

c = a < b
print(c) 



