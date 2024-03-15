import playingCards

class Bingo:
    def __init__(self) -> None:
        self.__rows = [[],[],[],[],[]]
        self.__play_mode = "L"
    
    def __str__(self) -> str:
        all_cards = ""
        for row in self.__rows:
            for card in row:
                all_cards += str(card) + " "
            all_cards += "\n"  # Add a line break after each row
        return all_cards[:-1]  # Removing the trailing newline

    def get_rows(self):
        return self.__rows


    def populate(self, cards, playMode) -> None:
        assert playMode in {"L", "C", "F"}, "PlayMode must be 'L', 'C', or 'F'"
        assert all(isinstance(card, playingCards.Card) for card in cards), "Only playing cards can be populated to a bingo grid"
        assert len(cards) <= 25, "Number of cards provided exceeds the maximum limit of 25"

        self.__play_mode = playMode

        count = 0
        for row in self.__rows:
            for column in range(5):
                if count < len(cards):  # Ensure we don't exceed the length of the cards list
                    if row == self.__rows[2] and column == 2:
                        if cards[count].isFaceUp(): cards[count].turnOver() 
                    else:
                        if not cards[count].isFaceUp(): cards[count].turnOver()  
                    row.append(cards[count])
                    count += 1
                else:
                    return  # Stop populating if the grid is full

    def search(self, card, rankOnly):
        assert isinstance(card, playingCards.Card), "Only a playing card can be used to search a bingo grid"
        assert isinstance(rankOnly, bool), "rankOnly must be a boolean"

        for row in self.__rows:
            for populated_card in row:
                if rankOnly:
                    if card.getRank() == populated_card.getRank():
                        if populated_card.isFaceUp(): populated_card.turnOver() 
                        return True
                else:
                    if card == populated_card:
                        if populated_card.isFaceUp(): populated_card.turnOver()
                        return True
        return False
    
    def isBingo(self):
        if self.__play_mode == L:
            for row in self.__rows:
                    if all(not row.isFaceUp):
                        return True
 
 
 """   
isBingo() – returns True if the face down cards in the bingo grid match the pattern specified by the 
play mode; returns False otherwise.  If the play mode is 'L', the face down cards must form at least one 
line of 5 face down cards, where the line can be horizontal, vertical, or diagonal.  If the play mode is 'C', 
there must be a face down card in all four corners of the bingo grid.  If the play mode is 'F', all cards in 
the bingo grid must be face down.
"""
def main():
    bingo1 = Bingo()
    
    # Make a 25 card bingo deck to populate with
    rank_set = set("23456789TJQKA")
    suit_set = set("SHDC")
    card_list = []
    for suit in suit_set:
        for rank in rank_set:
            if len(card_list) >= 25:
                break
            card_list.append(playingCards.Card(rank, suit, True))

    
    bingo1.populate(card_list,"L")
    print(str(bingo1))
    #print(bingo1.get_rows()[1][1].isFaceUp())
    print("is 4C in the populated cards?: ", bingo1.search(playingCards.Card("4","C",True),False))
    print("is 8H in the populated cards?: ", bingo1.search(playingCards.Card("8","H",True),False))
    print(str(bingo1))

if __name__ == "__main__":
    main()
