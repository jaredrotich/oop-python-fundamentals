class Pet:
    def speak(self):
        # print("sound made")
        return ("pet spoke")


Rasmus = Pet()
Rasmus.name = "Rasmus"  
print(Rasmus.name) 
print(Rasmus.speak())     

class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
       return f"{self.name} says woof! woof!"
    
koba = Dog("Koba","Great Dane", 3)
amad = Dog("amad", "Black Goat")
koba.age = 4
print(koba.speak())
print(koba.age)
print(amad.age)


class Cat:
    pass

class Rat:
    pass