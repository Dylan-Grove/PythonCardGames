import queues

class Card:
    """
    Represents a playing card.
    """
    def __init__(self, rank: str, suit: str, faceUp: bool) -> None:
        """
        Initializes a Card object.

        Parameters:
            rank (str): The rank of the card.
            suit (str): The suit of the card.
            faceUp (bool): Whether the card is face up or not.
        """
        assert rank in set("23456789tjqkaTJQKA"), "Card rank is invalid"
        assert suit in set("shdcSHDC"),           "Card suit is invalid"
        assert isinstance(faceUp, bool),          "faceUp must be a boolean"
        
        self.__rank   = rank.upper()
        self.__suit   = suit.upper()
        self.__faceUp = faceUp

    def __eq__(self, anotherCard: 'Card') -> bool:
        if isinstance(anotherCard, Card):
            return self.getRank() == anotherCard.getRank() and self.getSuit() == anotherCard.getSuit()
        return False
    
    def __str__(self) -> str:
        return f"[ {self.__rank}{self.__suit} ]"

    def getRank(self) -> str:
        return self.__rank
    
    def getSuit(self) -> str:
        return self.__suit
    
    def isFaceUp(self) -> bool:
        return self.__faceUp
    
    def turnOver(self) -> None:
        self.__faceUp = not self.__faceUp


class Deck:
    """
    Represents a deck of playing cards.
    """
    def __init__(self) -> None:
        self.__deck = queues.CircularQueue(52)
    
    def __str__(self) -> str:
        top_card = str(self.__deck.peek())
        all_cards = ", ".join(str(card) for card in self.__getCards())
        return f"Top card: {top_card}, All cards: {all_cards}"
    
    def addCard(self, card: Card) -> None:
        """
        Adds a card to the deck.

        Parameters:
            card (Card): The card to add.
        """
        assert isinstance(card, Card), "Can only add cards to deck"
        if not self.__deck.isFull():
            if card.isFaceUp():
                card.turnOver()
            self.__deck.enqueue(card)
        else:
            raise Exception(f"Cannot add {card}, Deck is full")

    def dealCard(self) -> Card:
        """
        Deals a card from the deck.

        Returns:
            Card: The dealt card.
        """
        if not self.__deck.isEmpty():
            dealt_card = self.__deck.dequeue()
            if not dealt_card.isFaceUp():
                dealt_card.turnOver()
            return dealt_card
        else:
            raise Exception("Cannot deal card from empty deck")
    
    def deckSize(self) -> int:
        """
        Returns the number of cards in the deck.

        Returns:
            int: The number of cards.
        """
        return self.__deck.size()
    
    def isComplete(self) -> bool:
        """
        Checks if the deck is complete.

        Returns:
            bool: True if the deck is complete, False otherwise.
        """
        if self.deckSize() != 52:
            return False
        
        rank_set = set("23456789TJQKA")
        suit_set = set("SHDC")
        deck_cards = self.__getCards()

        for suit in suit_set:
            for rank in rank_set:
                if Card(rank, suit, True) not in deck_cards:
                    return False
        
        return True
    
    def __getCards(self) -> list:
        """Returns a list of cards in the deck."""
        cards = []
        temp_queue = queues.CircularQueue(self.deckSize())

        # Dequeue cards from the deck and enqueue them into a temporary queue
        while not self.__deck.isEmpty():
            card = self.__deck.dequeue()
            cards.append(card)
            temp_queue.enqueue(card)

        # Restore the original order of cards in the deck
        while not temp_queue.isEmpty():
            self.__deck.enqueue(temp_queue.dequeue())

        return cards


def main():
    card1 = Card("2", "s", True)
    card2 = Card("3", "H", False)

    print("card1 rank and suit:", card1.getRank(), card1.getSuit())
    print("card2 rank and suit:", card2.getRank(), card2.getSuit())
    print("card1 is face up?", card1.isFaceUp())
    print("Turn over card1...")
    card1.turnOver()
    print("card1 is face up?", card1.isFaceUp())
    print("Is card1 the same as card1?", card1 == card1)
    print("Is card1 the same as card2?", card1 == card2)
    print("Is string fart the same as card2?", card2 == "fart")
    print("card1 formated as a string:", card1)

    deck = Deck()
    deck.addCard(card1)
    print(str(deck))
    deck.addCard(card2)
    print(str(deck))
    print(deck.dealCard())
    print(deck.dealCard())
    
    print("making deck2...")
    deck2 = Deck()
    deck2.addCard(card1)
    deck2.addCard(card2)
    print(str(deck2))
    print("is deck2 complete?", deck2.isComplete())

    # make a full deck for testing
    rank_set = set("23456789TJQKA")
    suit_set = set("SHDC")
    complete_deck = Deck()
    for suit in suit_set:
        for rank in rank_set:
            complete_deck.addCard(Card(rank, suit, True)) 

    print("is complete deck complete?", complete_deck.isComplete())

if __name__ == "__main__":
    main()
