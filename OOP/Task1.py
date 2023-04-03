# Create a class named Car that has the following attributes: make, model, and year. 
# It should also have a method called get_info() that returns a string with the car's make, model, and year.

# 1.
# class car():

#     def set_info(self, make, model, year):
#       self.make = make
#       self.model = model
#       self.year = year

#     def get_info(self):
#         print("Car`s make is", self.make)
#         print("Car`s model is", self.model)
#         print("Car`s year is", self.year)
    
# newCar = car()
# newCar.set_info("BMW","X5",2023)
# newCar.get_info()

# 2.
class car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print("Car`s make is", self.make)
        print("Car`s model is", self.model)
        print("Car`s year is", self.year)
    
newCar = car("BMW","X5",2023)
newCar.get_info()





