# Credit Card Management System

## 📌 Purpose

The main purpose of this project is **to practice implementing Python’s built-in list methods using custom logic**. Instead of relying on Python’s built-in `list` methods directly, I have re-created their functionality (like `append`, `insert`, `remove`, `pop`, `index`, etc.) in my own class `CreditCardList`.

This helps in:

- Understanding how Python list operations work internally.
- Gaining deeper control over data storage and manipulation.
- Practicing object-oriented programming concepts in Python.

---

## 🚀 Features

- **Custom `CreditCard` Class**

  - Stores credit card details (like account number, etc.).
  - Includes validation logic for account numbers.

- **Custom `CreditCardList` Class**
  - Re-implements Python list methods such as:
    - `append()` → Add a card to the end.
    - `extend()` → Add multiple cards.
    - `insert()` → Insert a card at a specific position.
    - `remove()` → Remove card by account number.
    - `delete()` → Delete card by index.
    - `pop()` → Remove and return card at an index.
    - `index()` → Find card index by account number.
    - `clear()` → Remove all cards.
  - Supports **negative indexing** (like Python lists).
  - Partial support for **slicing** (`__getitem__`).
  - Duplicate account numbers are **not allowed**.

---

## 📂 Project Structure

```
credit_card_management_system/
│── credit_card/
│   └── Credit_Card.py     # Defines CreditCard class with validation
│── credit_card_list/
│   └── CC_List.py      # Defines custom list class (CreditCardList)
│── main.py                # Example usage / testing
│── README.md              # Project documentation
```

---

## 🔧 Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/GhulamQadir/Credit-Card-Management-System.git
   cd Credit-Card-Management-System
   ```

2. Run the project:

   ```bash
   python main.py
   ```

3. Example (basic usage):

   ```python
   from credit_card.Credit_Card import CreditCard
   from CreditCardList import CreditCardList

   # Create cards
   card1 = CreditCard("Ali","Meezan bank","","123456789012345", 20000)
   card2 = CreditCard("Shahid","Bank Alfalah","987654321098765",9000)

   # Create custom list
   c_list = CreditCardList()
   c_list.append(card1)
   c_list.append(card2)

   print(c_list)  # Print all cards
   ```

---

## 🧑‍💻 Learning Outcome

Through this project, I practiced:

- Overriding **magic methods** (`__getitem__`, `__setitem__`, `__len__`, `__str__`).
- Designing **custom data structures** in Python.
- Input validation (e.g., checking account number format).
- Understanding how **Python’s list methods** work behind the scenes.

---

## 📜 License

This project is for **educational purposes** only.
