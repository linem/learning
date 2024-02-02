
class Parent:
    hair_color = "brown"        # child class will inherit the attribute hair color brown
    speaks = ["English"]

class Child(Parent):
    hair_color = "purple"       # child class can override inherited attribute

    def __init__(self):
        super().__init__()
        self.speaks.append("German")

print(Child.hair_color)
print(Parent.speaks)

### ------------------------------------------- ###

class Dog:                          # parent class
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

 #   def speak(self, sound):
 #       return f"{self.name} says {sound}"
    def speak(self, sound):
        return f"{self.name} barks {sound}"


class JackRussellTerrier(Dog):         # child class, CamelCase naming
#    def speak(self, sound = "Arf"):   # overrides parent speak      
#        return f"{self.name} says {sound}"
    def speak(self, sound = "Arf"):    # keeps changes to parent speak
        return super().speak(sound)    # access parent class by using super()
                                       # calling super().speak(sound) searches \
                                       # parent class for .speak() and calls it \
                                       # with the variable sound

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(type(miles))                # <class '__main__.JackRussellTerrier'>
print(isinstance(miles, Dog))     # checks if miles is instance of Dog class TRUE
                                  # miles is both a Dog instance and a JackRusselTerrier instance

print(miles.speak())              # by default miles says Arf
print(miles.speak("Grrr"))        # but miles can also say Grrr

print(miles.speak())              # after changing the child method
print(miles.speak("Grrr"))        # using super() the formatting from the
                                  # parent class is used (changed says to barks)
