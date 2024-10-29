# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name  # Initialize name
        self.age = age    # Initialize age

    def speak(self):
        return f"{self.name} makes a sound."

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        # Call the parent class's __init__ method to initialize 'name' and 'age'
        super().__init__(name, age)
        self.breed = breed  # Initialize additional variable unique to Dog

    def speak(self):
        return f"{self.name} barks."

# Create instances
animal = Animal("Generic Animal", 5)
dog = Dog("Buddy", 3, "Golden Retriever")

print(animal.speak())   # Output: "Generic Animal makes a sound."
print(dog.speak())      # Output: "Buddy barks."
print(dog.breed)        # Output: "Golden Retriever"
