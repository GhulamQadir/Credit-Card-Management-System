from credit_card.Credit_Card import CreditCard


class CreditCardList:
    def __init__(self):
        self.__credit_cards = []

    def _verify_instance(self, c_card):
        if not isinstance(c_card, CreditCard):
            raise TypeError("The card must be of type CreditCard")

    def add(self, c_card: CreditCard):
        self._verify_instance(c_card)
        temp_list = [None] * (len(self.__credit_cards) + 1)
        for i in range(len(temp_list) - 1):
            temp_list[i] = self.__credit_cards[i]

        temp_list[-1] = c_card
        self.__credit_cards = temp_list

    def add_collection(self, *c_cards):
        for card in c_cards:
            self.add(card)

    def insert_card(self, index, c_card: CreditCard):
        self._verify_instance(c_card)
        temp_list = [None] * (len(self.__credit_cards) + 1)
        print(temp_list)
        i = 0
        global_cards_index = 0
        while i < len(temp_list):
            if i==index:
                temp_list[i] = c_card
                temp_list[i + 1] = self.__credit_cards[global_cards_index]
                i += 2
                global_cards_index += 1
            else:
                temp_list[i] = self.__credit_cards[global_cards_index]
                i += 1
                global_cards_index += 1

        self.__credit_cards = temp_list

        # if index <0:
        #     if len(self.__credit_cards)-index<0:
        #         self.

    def __str__(self):
        string = ""
        for card in self.__credit_cards:
            string += f"{str(card)}\n"
        return string
