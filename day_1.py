# Date : march 3 2023

class Person:
    name = "Harshad"
    age = 27

# type of class defined is 'type'
print(type(Person))

# there are some attributes which store  the state of a type object
print(Person.__name__)

# there are some methods --> below method creates instance of the defiend class
# person = Person()

print(type(Person))

print(Person.name)
print(getattr(Person,'name'))
# print(getattr(Person,'x'))
print(setattr(Person,'address','Mumbai'))
print(Person.__dict__)


