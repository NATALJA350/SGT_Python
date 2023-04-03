# Create a class named Animal that has the following attributes: name and species. 
# It should also have a method called speak() that returns a string with the animal's sound.

species=input("Enter animal`s type dog or cat: ")
name=input("Enter animal`s name: ")

class Animal:
    def __init__(self, name, species):
       self.name = name
       self.species = species
       if species == "dog":
            self.sound = "woof" 
       else:
            self.sound = "miau"
           
    def speak(self):
        print("Enter animal species and: ")
    def __str__(self):
        return"{} is a {} with the sound {}".format(self.name,self.species, self.sound)

animal = Animal(name, species)
print(animal)
