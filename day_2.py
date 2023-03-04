# callable class attributes --> functions

class Program:
    language = 'Python'


    def say_hello(self):
        print(f"hello from {Program.language}")

print(Program.__dict__)
Program.say_hello(Program)

print('*'*50)
# class are callable namespace diff
class BankAccount:
    interest = 8
    saving = 100


b1 = BankAccount()
b2 = BankAccount()
print(BankAccount.__dict__)

b1.saving = 50
print(b1.__dict__)
print(b1.interest)
print(b1.saving)

b2.interest = 10
print(b2.__dict__)
print(b2.interest)
print(b2.saving)

print('*'*50)

# function attributes

class Myclass:

    def say_hello(self):
        print("hello")

my_obj = Myclass()

print(Myclass.__dict__)
print(my_obj.__dict__)

