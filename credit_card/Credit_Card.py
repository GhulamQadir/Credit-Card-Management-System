class CreditCard:
    def __init__(self, customer_name, bank, account_no, limit):
        self.__customer_name = customer_name
        self.__bank = bank
        self.__account_no = account_no
        self.__limit = limit
        self.__balance = 0

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def bank(self):
        return self.__bank

    @property
    def account_no(self):
        return self.__account_no

    @property
    def limit(self):
        return self.__limit

    @property
    def balance(self):
        return self.__balance

    def charge(self, price):
        try:
            price_to_charge = float(price)
        except ValueError:
            raise ValueError("Price must be an integer or float")
        if price_to_charge <= 0:
            raise ValueError("Price must be greater than zero")
        if price_to_charge + self.__balance > self.__limit:
            return False
        self.__balance += price_to_charge

    def make_payment(self, amount):
        try:
            user_amount = float(amount)
            print(user_amount)
        except TypeError:
            raise TypeError("Price must be an integer or float")
        self.__balance -= user_amount

    def __str__(self):
        return f"Name: {self.__customer_name}, Bank: {self.__bank}, Balance: {self.__balance}"


cc = CreditCard("Ali", "Meezan Bank", "323 989 323 7827", 4000)
cc.charge(3400)
cc.make_payment(300)
