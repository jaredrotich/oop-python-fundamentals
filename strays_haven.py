#Class initialisation with default __init__
class Pet:

    #This is the Parent & base class for all pets
    def __init__(self, name, age=None):
        #Protected attributes(encapsulation)
        self._name = name
        self._age = age

    # Getter and setter methods for encapsulation
    def get_age(self):
        print ("Retrieving age")
        return self._age
    
    def set_age(self, age):
        if type(age) in (int, float) and (age >= 0 and age <=120):
            self._age = age
        else:
            print("Age must be greater than 0 or less than 120")

    # encapsulated age property
    age = property(get_age, set_age)

    def speak(self):
        print("sound made")
        return ("pet spoke")
        

    def describe(self):
        if self._age:
            return f"{self._name} is {self._age} years old."
        else:
            return f"{self._name}'s age is unknown."


#A simple class to represent a dog with modified __init__   
class Dog(Pet):

    species = "canis lupus familiaris" # class attribute

    def __init__(self,name,breed,age="N/A"):
        super().__init__(name, age)
        # instance attribute
        self.breed = breed
        

    # override parent's speak method
    def speak(self):
        return f"{self._name} says woof! woof!"

#Cat is a subclass of Pet(inheritance)   
class Cat(Pet):
    
    def __init__(self, name, owner, age=None):

        #call parent's or superclass' initialiser method (inheritance)
        super().__init__(name, age)
        self._owner = owner

    def speak(self):
        return f"{self._name} meows!"

    def get_owner(self):
        return self._owner
    
    def set_owner(self, owner):
        self._owner = owner

    owner = property(get_owner, set_owner)


class Rat(Pet):
    species = "rattus norvegicus"

    def __init__(self,name, owner, age=False):

        super().__init__(name, age)
        self._owner = owner
    
    #overriding parents speak method

    def speak(self):
        return f"{self._name} squeals!"

rasmus = Pet("Scooby")
rasmus.name = "Rasmus"
print(rasmus.name)
print(rasmus.speak())

koba = Dog("Koba","Great Dane", 3)
amad = Dog("amad", "Black Goat") # works because we intialised age with a default value
koba.age = 4
print(koba.speak())
print(koba._age)
print(amad._age)
print(amad.species)
print(amad._name)

print(koba.species)
print(koba._name)

#demonstrating encapsulation 
print(f"Pet's age: {rasmus.age}")
rasmus.age = 5
print(f"Pet's new age: {rasmus.age}")

#demonstrating inheritance
whiskers = Cat("Whiskers", "Juanita", 6)
print(whiskers.describe())

#demonstrating polymorphism
jerry = Rat("Jerry", "Abdirahman Ali", 4)
print(rasmus.speak())
print(koba.speak())
print(whiskers.speak())
print(jerry.speak())
