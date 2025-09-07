class CreditCard:
    """
    A class that models a simple Credit Card system.

    Features:
    - Store customer, bank, account, limit, and balance details.
    - Allow charges to be added if within the limit.
    - Allow payments to be made to reduce the balance.
    - Provide a readable string representation of the card.
    """

    def __init__(self, customer_name, bank, account_no, limit):
        """
        Initialize a new CreditCard object.

        Args:
            customer_name (str): The cardholder's name.
            bank (str): The bank's name.
            account_no (str): The credit card account number.
            limit (float/int): The credit card spending limit.
        """
        self.__customer_name = customer_name  # Private attribute: cardholder’s name
        self.__bank = bank  # bank name
        self.__account_no = account_no  # account number
        self.__limit = limit  # spending limit
        self.__balance = 0  # initial balance set to 0

    # ---- Properties (read-only getters) ----
    @property
    def customer_name(self):
        """Return the customer name (read-only)."""
        return self.__customer_name

    @property
    def bank(self):
        """Return the bank name (read-only)."""
        return self.__bank

    @property
    def account_no(self):
        """Return the account number (read-only)."""
        return self.__account_no

    @property
    def limit(self):
        """Return the credit limit (read-only)."""
        return self.__limit

    @property
    def balance(self):
        """Return the current balance (read-only)."""
        return self.__balance

    # ---- Methods ----

    def charge(self, price):
        """
        Attempt to charge (add) an amount to the card balance.

        Args:
            price (int/float/str): The amount to charge.

        Returns:
            bool: False if the charge exceeds the limit, True/None otherwise.

        Raises:
            ValueError: If price is not a number or is <= 0.
        """
        try:
            price_to_charge = float(
                price
            )  # Convert input to float (string like "23" also works)
        except ValueError:
            raise ValueError(
                "Price must be an integer or float"
            )  # Error if conversion fails

        if price_to_charge <= 0:  # Ensure price is positive
            raise ValueError("Price must be greater than zero")
        if price_to_charge + self.__balance > self.__limit:
            raise ValueError(
                "You cannot exceed your card limit"
            )  # Raise error if it would exceed limit
        self.__balance += price_to_charge  # Otherwise, add price to balance

    def make_payment(self, amount):
        """
        Make a payment to reduce the card balance.

        Args:
            amount (int/float/str): The payment amount.

        Raises:
            TypeError: If the amount cannot be converted to float.
        """
        try:
            user_amount = float(amount)  # Convert input to float
        except TypeError:
            raise TypeError("Price must be an integer or float")

        self.__balance -= user_amount  # Subtract payment from balance

    def __str__(self):
        """
        Return a user-friendly string representation of the CreditCard.
        """
        return f"Name: {self.__customer_name}, Bank: {self.__bank}, Balance: {self.__balance}"
