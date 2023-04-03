# Create a class named Rectangle that has the following attributes: width and height. 
# It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively.

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)

width=int(input("Enter width: "))
height=int(input("Enter height: "))

result = Rectangle(width,height)
print("Area: ", result.area())
print("Perimeter: ", result.perimeter())
