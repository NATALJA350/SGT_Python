# Create a class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address.

class Person:
    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        print("Person`s name, age, and address are: ", self.name,"/", self.age,"/", self.address)
    
person1 = Person("John", "25", "Main str 1")
person1.get_info()