# # 7/3/2023
# # initializing class instance
#
# class Person:
#     name = 'Harshad'
#
#     def __init__(self, age):
#         self.age = age
#
# print(Person.__dict__)
# p = Person(12)
# print(p.__dict__)
#


from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()