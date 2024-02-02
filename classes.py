
class Dog:
    species = "Canis familiaris"    # class attribute  (all instances will have this)

    def __init__(self, name, age):  # initializes a new instance of the class
        self.name = name            # creates an instance attribute and assigns a value
        self.age = age

    def __str__(self):              # special instance method
        return f"{self.name} is {self.age} years old" 

    def description(self):          # instance method
        return f"{self.name} is {self.age} years old"  
    
    def speak(self, sound):         # instance method
        return f"{self.name} says {sound}"     


miles = Dog("Miles", 4)             # instantiates Dog class and creates an object
buddy = Dog("Buddy", 9)

print(miles)                        # prints the memory address of the stored object
print(miles.name)                   # prints the value of the instance attribute name
print(miles.species)                # prints the value of the class attribute

miles.species = "Felis silvestris"  # values can change, ie objects are mutable
print(miles.species)                # changed species value
print(buddy.species)                # still has initial species value

print(miles.description())          # instance method returns string
print(miles.speak("Woof"))
print(miles.speak("Bow Wow"))

print(miles)                        # after adding __str__ method the string is \
                                    # printed instead of the memory adress

print(Dog.species)                  # you can print class attributes without instantiating an object
