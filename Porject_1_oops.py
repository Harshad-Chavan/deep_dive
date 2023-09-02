import decimal
from datetime import datetime

global_account_set = set()


class Account:

    transaction_type = {"deposit": "D", "withdrawal": "W", "interest_deposit": "I", "declined": "X"}
    global_transaction_id = 0

    def __init__(self, account_number, first_name, last_name):
        self.account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._balance = 0.0

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if value in global_account_set:
            raise Exception("Account number already Exists")
        global_account_set.add(value)
        self._account_number = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def deposit(self, amount):
        if amount < 0:
            return self.generate_confirmation_number("declined", self.account_number)
        else:
            self.balance = self.balance + amount
            return self.generate_confirmation_number("deposit", self.account_number)

    def withdrawal(self, amount):
        if amount < 0:
            return self.generate_confirmation_number("declined", self.account_number)
        else:
            self.balance = self.balance - amount
            return self.generate_confirmation_number("withdrawal", self.account_number)

    @classmethod
    def generate_confirmation_number(cls, type, acc_num):
        current_date_time = datetime.now().utcnow()
        cls.global_transaction_id += 1
        return f"{cls.transaction_type[type]}-{acc_num}-{current_date_time}-{cls.global_transaction_id}"


class Timezone:
    pass


acc_1 = Account(1234, "Harshad", "Chavan")
acc_2 = Account(1235, "Harshad", "Chavan")

print(acc_1.account_number)
print(acc_2.account_number)

print(acc_1.balance)
print(acc_2.balance)

print(acc_1.deposit(100))
print(acc_2.deposit(50))

print(acc_1.withdrawal(50))
print(acc_2.withdrawal(30))

print(acc_1.balance)
print(acc_2.balance)
