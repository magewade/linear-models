class Client:
    default_name = "Default Client"
    default_age = 30

    __slots__ = ("name", "age", "_house", "_account")

    def __init__(self, name=default_name, age=default_age, bank=None):
        self.name = name
        self.age = age
        self._house = None
        self._account = bank.add_account(self) if bank else None

    def info(self):
        print(
            f"Name: {self.name}, Age: {self.age}, House: {self._house is not None}, Balance: {self._account.balance if self._account else 0}"
        )

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, House: {self._house}, Account balance: {self._account.balance if self._account else 0}"

    @staticmethod
    def default_info():
        print(
            f"Default name: {Client.default_name}, Default age: {Client.default_age}"
        )

    def _make_deal(self, house, price):
        self._account -= price
        self._house = house

    def earn_money(self, amount):
        self._account += amount

    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        if self._account.balance >= final_price:
            self._make_deal(house, final_price)
        else:
            print(
                f"Not enough money to buy the house. Required: {final_price}, but only {self._account.balance} on the account."
            )


class Account:
    __slots__ = ("client", "balance")

    def __init__(self, client, balance=0):
        self.client = client
        self.balance = balance

    def __str__(self):
        return f"Account of {self.client.name}, Balance: {self.balance}"

    def __iadd__(self, amount):
        self.balance += amount
        return self

    def __isub__(self, amount):
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        return self


class Bank:
    def __init__(self):
        self._accounts = []

    def add_account(self, client):
        for account in self._accounts:
            if account.client == client:
                raise Exception("Client already has an account in this bank!")
        account = Account(client)
        self._accounts.append(account)
        return account

    def __str__(self):
        return "\n".join([str(account) for account in self._accounts])


class House:
    __slots__ = ("_area", "_price")

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    __slots__ = ()

    def __init__(self, price):
        super().__init__(area=42, price=price)

