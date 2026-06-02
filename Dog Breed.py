class Dog:
    species = "dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Tommy = Dog("Tommy", 12)
Ryely = Dog("Ryely", 15)

print("Tommy is a {}".format(Tommy.species))
print("Ryely is a {}".format(Ryely.species))
print("{} is {} years old".format(Tommy.name, Tommy.age))
print("{} is {} years old".format(Ryely.name, Ryely.age))