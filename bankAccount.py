class BankAccount:
    types = ["Checking", "Savings"]
    
    def __init__(self, type, name, balance):

        self.type = type
        self.name = name
        self.balance = balance
    
    def __str__(self):
        return f"{self.name}'s {self.type} Account has a balance of ${self.balance}"
    
    @property
    def type(self):
         return self._type

    @type.setter
    def type(self, type):
        if type not in self.types:
            raise ValueError("Invalid Account Type")
        self._type = type

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Balance must be Greater than 0")
        self._balance = balance


    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Invalid Amount")
        else:
            self._balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid Amount")
        self._balance += amount
    
    def __add__(self, other):
        balance = self.balance + other.balance
        return BankAccount("Checking", "b", balance)


class Checking(BankAccount):
    def __init__(self, name, balance,type = "Checking"):
        super().__init__(type, name, balance)
    def __str__(self):
        return f"THIS IS {self.name}'s CHECKINGS ACCOUNT with ${self.balance}"

class Savings(BankAccount):
    def __init__(self, name, balance, type = "Savings"):
        super().__init__(type, name, balance)
    def __str__(self):
        return f"THIS IS {self.name}'s SAVINGS ACCOUNT with ${self.balance}"
