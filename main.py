from credit_card.Credit_Card import CreditCard
from credit_card_list.CC_List import CreditCardList


def main():
    # Create a CreditCard instance for Ali with a limit of 4000
    cc = CreditCard("Ali", "Meezan Bank", "323 989 323 782 665", 4000)

    # Create an empty CreditCardList object
    cards_list = CreditCardList()
    # Append the previously created CreditCard (Ali) to the list
    cards_list.append(cc)

    # Extend the list with multiple new CreditCard instances
    cards_list.extend(
        [
            CreditCard("Shahid", "HBL", "173 069 126 333 009", 8000),
            CreditCard("Umer", "Faysal Bank", "887 223 173 691 263", 12000),
            CreditCard("Umer", "Meezan Bank", "240 349 232 778 887", 12000),
        ]
    )
    print(cards_list)

    # Get the index of the card with number "1730691263" between positions -80 and 10
    # get_index = cards_list.index("173 069 1263", -80, 10)
    # print(get_index)

    # Slice the cards_list from index 1 to 9 (like normal Python list slicing)
    sliced_list = cards_list[1:9]
    print("sliced_list: ", sliced_list)

    # Remove the CreditCard with number "173691263" from the list
    cards_list.remove("323 989 323 782 665")
    print(cards_list)

    # Insert a new CreditCard (Zahid) at index 1
    cards_list.insert(
        1, CreditCard("Zahid", "Bank Alfalah", "323 989 323 213 817", 4000)
    )
    print(cards_list)

    # Delete the CreditCard at index 2
    cards_list.delete(2)
    print(cards_list)

    # Remove the last CreditCard from the list (pop)
    cards_list.pop()
    print(cards_list)


if __name__ == "__main__":
    main()
