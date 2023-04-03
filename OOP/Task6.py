# Create a base class named Vehicle that has the following attributes: make, model, and year. 
# It should also have a method called get_info() that returns a string with the vehicle's make, model, and year. 
# Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle.

class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
       return str(self.make), str(self.model), str(self.year)

class Car(Vehicle):
    def __init__(self, make, model, year, colour):
        super().__init__(make, model, year)
        self.colour = colour

    def get_info_car(self):
       return"The car`s make, model, year and colour are: {}, {}, {}, {}".format(self.make,self.model, self.year, self.colour)

class Truck(Vehicle):
    def __init__(self, make, model, year, weights):
        super().__init__(make, model, year)
        self.weights = weights

    def get_info_truck(self):
       return"The truck`s make, model, year and weights are: {}, {}, {}, {}".format(self.make,self.model, self.year, self.weights)

car1=Car("BMW", "X5", 2023, "black")
truck1=Truck("Mercedes-Benz", "Atego", 2013, "16 t.")

print(car1.get_info_car())
print(truck1.get_info_truck())
        