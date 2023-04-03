# Create a base class named Person that has the following attributes: name, age, and address. 
# It should also have a method called get_info() that returns a string with the person's name, age, and address. 
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods specific to each role.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        return f"Person`s name is {self.name}, person`s age is {self.age} and address {self.address}"

class Student(Person):
    def __init__(self, name, age, address, course, language):
        super().__init__(name, age, address)
        self.course = course
        self.language = language

    def student_info(self):
        return f"The student {self.name} takes the course {self.course} in {self.language}"

class Teacher(Person):
    def __init__(self, name, age, address, course, language):
        super().__init__(name, age, address)
        self.course = course
        self.language = language

    def teacher_info(self):
        return f"The teacher {self.name} teaches the course {self.course} in {self.language}"

student1=Student("Natalja", 30, "Riga", "Python", "English")
teacher1=Teacher("Arturs", 30, "Riga", "Python", "English")

print(student1.student_info())
print(teacher1.teacher_info())