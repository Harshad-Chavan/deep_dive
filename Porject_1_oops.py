import decimal
import numbers
from datetime import datetime, timedelta
import itertools

global_account_set = set()


class Account:

    transaction_type = {"deposit": "D", "withdrawal": "W", "interest_deposit": "I", "declined": "X"}

    # using the itertools.count instead of a variable this is a kind of generator
    global_transaction_id = itertools.count(0)

    _interest_rate = 0.5

    def __init__(self, account_number, first_name, last_name, initial_balance=0, timezone=None):
        self._account_number = account_number
        self._first_name = first_name
        self._last_name = last_name
        self._balance = float(initial_balance)

        if timezone is None:
            timezone = Timezone("UTC", 0, 0)
        self.timezone = timezone

    @staticmethod
    def validate_name(value, field_title):
        if value is None or len(value.strip()) == 0:
            raise ValueError(f"{field_title} cannot be empty")
        return value

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
        # adding some validation
        self._first_name = Account.validate_name(value, "First name")

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def last_name(self, value):
        # adding some validation
        self._last_name = Account.validate_name(value, "Last name")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, Timezone):
            raise ValueError("Time Zone must be a valid TimeZone object.")
        self._timezone = value

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            return self.generate_confirmation_number("declined", self.account_number)
        else:
            self._balance = self._balance + amount
            return self.generate_confirmation_number("deposit", self.account_number)

    def withdrawal(self, amount):
        if self.balance == 0 or (self.balance - amount) < 0 or amount < 0:
            return self.generate_confirmation_number("declined", self.account_number)
        else:
            self._balance = self._balance - amount
            return self.generate_confirmation_number("withdrawal", self.account_number)

    def deposit_interest(self):
        interest_amount = self.balance * (Account.get_interest_rate() / 100)
        self.deposit(interest_amount)
        return self.generate_confirmation_number("interest_deposit", self.account_number)

    @classmethod
    def generate_confirmation_number(cls, transaction_type, acc_num):
        current_date_time = datetime.now().utcnow().strftime("%Y%m%d%H%M%S")
        return (
            f"{cls.transaction_type[transaction_type]}-{acc_num}-{current_date_time}-{next(cls.global_transaction_id)}"
        )

    def generate_confirmation_number_object(self, code):
        class ConfirmationCode:
            def __init__(self, code):
                self.transaction_code, self.account_number, self.time_utc, self.transaction_id = code.split("-")

        return ConfirmationCode(code)

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError("Interest must be a real number")
        if value < 0:
            raise ValueError("Interest cannot be Negative")
        cls._interest_rate = value


class Timezone:
    def __init__(self, name, offset_hours, offset_mins):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError("Timezone name cannot be empty.")
        self._name = str(name)

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError("offset hours must be an integer")

        if not isinstance(offset_mins, numbers.Integral):
            raise ValueError("offset mins must be an integer")

        if offset_mins > 59 or offset_mins < -59:
            raise ValueError("Minutes offset must be in betwwen -59 and 59 (inclusive)")

        offset = timedelta(hours=offset_hours, minutes=offset_mins)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError("Offset must be between -12:00 to 14:00")

        self._offset_hours = offset_hours
        self._offset_mins = offset_mins
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return isinstance(other, Timezone) & self.name == other.name & self.offset == other.offset

    def __repr__(self):
        return f"Timezone(name:{self.name},offset_hours={self._offset_hours},offset_mins={self._offset_mins})"


acc_1 = Account(1235, "Harshad", "Chavan")
acc_2 = Account(1234, "Nivi", "Chavan")

print(acc_1.account_number)
print(acc_2.account_number)

print(acc_1.balance)
print(acc_2.balance)

print(acc_1.deposit(100))
print(acc_2.deposit(50))

print(acc_1.deposit_interest())
print(acc_2.deposit_interest())

print(acc_1.withdrawal(50))
print(acc_2.withdrawal(30))

print(acc_1.balance)
print(acc_2.balance)

print(acc_1.withdrawal(50))
print(acc_2.withdrawal(40))

print(acc_1.timezone)
