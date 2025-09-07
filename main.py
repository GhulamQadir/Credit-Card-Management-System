from credit_card.Credit_Card import CreditCard
from credit_card_list.CC_List import CreditCardList


def main():
    cc = CreditCard("Ali", "Meezan Bank", "323 989 323 7827", 4000)
    cards_list = CreditCardList()
    cards_list.add(cc)
    cards_list.add(CreditCard("Shahid", "HBL", "173691263", 8000))
    cards_list.add(CreditCard("Umer", "Faysal Bank", "173691263", 12000))
    # cards_list.add_collection(cc,CreditCard("Shahid", "HBL", "173691263", 8000))
    print(cards_list)
    cards_list.insert_card(2, CreditCard("Sameer", "UBL", "243423423", 9000))
    print(cards_list)


if __name__ == "__main__":
    main()
