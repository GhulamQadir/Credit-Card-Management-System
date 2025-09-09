from credit_card.Credit_Card import CreditCard


class CreditCardList:
    """
    A custom list-like container for CreditCard objects.
    Supports operations like append, extend, insert, delete, remove, pop, clear, and index search.
    """

    def __init__(self):
        """Initialize an empty CreditCardList."""
        self.__credit_cards = []

    # ------------------ Internal Helpers ------------------ #
    def _check_index_type(self, index):
        """Ensure the index is an integer."""
        if not isinstance(index, int):
            raise TypeError(f"Expects index of type int, not {type(index)}")

    def _verify_instance(self, c_card):
        """Ensure the object is a CreditCard instance."""
        if not isinstance(c_card, CreditCard):
            raise TypeError("The card must be an instance of CreditCard")

    def _is_duplicate_account(self, account_no: str):
        """
        Check for duplicate account numbers in the list.
        Raises ValueError if a duplicate is found.
        """
        for card in self:
            if account_no == card.account_no:
                raise ValueError(
                    f"A card with account number {account_no} already exists."
                )

        return False

    def _validate_index(self, index, for_index_method=False):
        """
        Validate and adjust a list index.

        Parameters:
            index (int): Index to validate.
            for_index_method (bool): If True, negative indices for index() method
                                     are converted to 0 instead of raising IndexError.

        Returns:
            int: Validated and adjusted index.
        """
        if index < 0:
            # Adjust negative index relative to the list length
            index = len(self) + index
            if not for_index_method and index < 0:
                # If index is still negative, raise an error for normal methods
                raise IndexError("List index out of range")
            elif for_index_method and index < 0:
                # For index() method, treat out-of-range negatives as 0
                index = 0
        return index

    # ------------------ Special Methods ------------------ #
    def __getitem__(self, index):
        """
        Retrieve element(s) by index or slice.
        Returns a CreditCard object for single index or a CreditCardList for a slice.
        """
        if not isinstance(index, (int, slice)):
            raise TypeError("List indices must be integers or slices")
        if isinstance(index, slice):
            new_instance = CreditCardList()
            sliced_list = self.__credit_cards[index]
            for card in sliced_list:
                new_instance.append(card)
            return new_instance
        return self.__credit_cards[index]

    def __setitem__(self, index, c_card: CreditCard):
        """Set a CreditCard object at a specific index."""
        self._check_index_type(index)
        self._verify_instance(c_card)
        self.__credit_cards[index] = c_card

    def __len__(self):
        """Return the number of CreditCard objects in the list."""
        return len(self.__credit_cards)

    def __str__(self):
        """Return a human-readable string of all cards in the list."""
        string = ""
        for card in self:
            string += f"{str(card)}\n"
        return string

    # ------------------ List-like Methods ------------------ #
    def append(self, c_card: CreditCard):
        """Append a CreditCard to the end of the list."""
        self._verify_instance(c_card)  # Ensure c_card is a CreditCard
        self._is_duplicate_account(
            c_card.account_no
        )  # Check no duplicate account numbers

        temp_list = [None] * (len(self) + 1)  # Create a new list larger by 1
        for i in range(len(temp_list) - 1):
            temp_list[i] = self[i]  # Copy existing cards to new list

        temp_list[-1] = c_card  # Add the new card at the last position
        self.__credit_cards = temp_list  # Replace the old list with new one

    def extend(self, c_cards: list):
        """Append multiple CreditCard objects from a list."""
        if not isinstance(c_cards, list):
            raise TypeError("Expects list of type CreditCard")
        for card in c_cards:
            self._verify_instance(card)  # Ensure each element is CreditCard
            self._is_duplicate_account(card.account_no)  # Check duplicates
            self.append(card)  # Append each card using existing append logic

    def insert(self, index, c_card: CreditCard):
        """Insert a CreditCard at a specific index, shifting elements to the right."""
        valid_index = self._validate_index(index)  # Validate index
        if valid_index > len(self) - 1:
            raise IndexError("List index out of range")
        self._verify_instance(c_card)
        self._is_duplicate_account(c_card.account_no)
        temp_list = [None] * (len(self) + 1)  # New list larger by 1
        i = 0
        global_cards_index = 0  # Tracks original list position
        while i < len(temp_list):
            if i == valid_index:
                temp_list[i] = c_card  # Insert new card at target index
                temp_list[i + 1] = self[global_cards_index]  # Shift next card
                i += 2  # Skip one extra because we inserted a new element
                global_cards_index += 1
            else:
                temp_list[i] = self[global_cards_index]  # Copy old card
                i += 1
                global_cards_index += 1

        self.__credit_cards = temp_list  # Replace old list with updated one

    def remove(self, account_no: str):
        """Remove the first CreditCard with the given account number."""
        if isinstance(account_no, str):
            # Remove any spaces from the account number string
            split_no = account_no.split()
            clean_account_no = "".join(split_no)
            try:
                # Ensure account number contains only digits
                valid_no = int(clean_account_no)
            except ValueError:
                raise ValueError("Account Number can contain digits only")
            match_found = False  # Flag to track if a match was removed

            # Make a copy of the current card list
            temp_list = [x for x in self]  # Copy existing list

            # Clear the original list to rebuild it without the removed card
            self.__credit_cards = []

            # Rebuild list while skipping the first matching card
            for card in temp_list:
                if card.account_no == valid_no and not match_found:
                    match_found = True  # Mark that we removed one match
                    continue  # Skip appending this card
                self.append(card)  # Append all other cards

            # If no card was found with the given account number, raise error
            if not match_found:
                raise ValueError(f"Card with AccountNo: {valid_no} Not Found!")

    def delete(self, index):
        """Delete the CreditCard at the specified index."""
        self._check_index_type(index)
        valid_index = self._validate_index(index)  # Ensure index is an integer
        if valid_index >= len(self):  # Validate index
            raise IndexError("List index out of range")

        temp_list = [x for x in self.__credit_cards]  # Copy existing cards
        self.__credit_cards = []  # Clear current list
        for i, card in enumerate(temp_list):
            if valid_index == i:
                continue  # Skip the card at the target index
            self.append(card)  # Rebuild the list without the deleted card

    def pop(self, index=-1):
        """Remove and return a CreditCard at the specified index (default last)."""
        self._check_index_type(index)  # Ensure index is an integer
        valid_index = self._validate_index(index)  # Adjust index
        temp_list = [x for x in self]  # Copy old list
        self.delete(valid_index)  # Remove card at index
        return temp_list[valid_index]  # Return removed card

    def clear(self):
        self.__credit_cards = []

    def index(self, account_no, start_index=0, end_index=None):
        """
        Return the index of the first CreditCard with the given account number
        between start_index and end_index.
        """
        if end_index == None:
            # If end_index not provided, search until the end of the list
            end_index = len(self)

        # Ensure both start and end indices are integers
        self._check_index_type(start_index)
        self._check_index_type(end_index)

        # Validate indices and adjust negatives
        start = self._validate_index(
            start_index, for_index_method=True
        )  # Negative start -> 0
        end = self._validate_index(end_index)  # validate end index

        # Ensure end does not exceed list length
        if end > len(self):
            end = len(self)

        # If start index is after or equal to end, the search range is invalid
        if start >= end:
            raise ValueError(f"{account_no} not in list")

        # Loop over the specified range to find the first matching card
        for i in range(start, end):
            if self[i].account_no == account_no:
                return i

        # If loop finishes without finding a match, raise an error
        raise ValueError(f"{account_no} is not in list")
