#----------------------------------------------------
# Assignment 3: Rigged Solitaire
# 
# Author: 
# Collaborators/References:
#----------------------------------------------------

class CardNode:
    VALID_SUITS = ['D', 'S', 'H', 'C']
    VALID_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    
    # DO NOT CHANGE __init__ method
    def __init__(self, rank, suit, faceUp = True):
        '''
        Initializes a doubly linked list node that stores information about a card. 
        Cards have a suit and rank, and may be face up or down. Asserts that the provided
        suit and rank are valid.

        Input:
          - rank (string): represents number 2-10, Jack, Queen, King, Ace
          - suit (string): represents spade, heart, diamond, or club
          - faceUp (Boolean): represents whether the card is face up (True) or face down (False)

        Returns: None
        '''        
        assert type(rank) == str, "Rank must be a string"
        assert type(suit) == str, "Suit must be a string"
        assert type(faceUp) == bool, "Visible must be boolean"
        
        assert len(suit) == 1, 'Suit must be a single character'
        assert len(rank) == 1, 'Rank must be a single character'
        
        suit = suit.upper()
        rank = rank.upper()
        assert (suit in CardNode.VALID_SUITS), "Invalid Suit provided: {}.".format(suit)
        assert (rank in CardNode.VALID_RANKS), "Invalid Rank provided: {}.".format(rank)
        
        self.__rank = rank
        self.__suit = suit
        self.__faceUp = faceUp
        self.__next = None
        self.__previous = None
    
    # DO NOT CHANGE getRank method   
    def getRank(self):
        '''Returns the rank of the card. No input.'''
        return self.__rank
    
    # DO NOT CHANGE getSuit method
    def getSuit(self):
        '''Returns the suit of the card. No input.'''
        return self.__suit
    
    # DO NOT CHANGE isFaceUp method
    def isFaceUp(self):
        '''Returns whether the card is face up (True) or down (False). No input.'''
        return self.__faceUp
    
    # DO NOT CHANGE turnOver method
    def turnOver(self):
        '''
        Changes the card from face up to face down, or from face down to face up.
        Input: N/A  
        Returns: None.
        '''
        self.__faceUp = not(self.__faceUp)
      
    # DO NOT CHANGE getNext method    
    def getNext(self):
        '''Returns the reference to whatever is next (either None or a CardNode). No input.'''
        return self.__next
    
    # DO NOT CHANGE setNext method
    def setNext(self, newNext):
        '''
        Updates the next reference.
        Input: newNext (None or a CardNode) - the object that will come next
        Returns: None
        '''        
        assert (isinstance(newNext, CardNode) or newNext==None),\
               'Cannot set next to {}'.format(type(newNext))
        self.__next = newNext
    
    # DO NOT CHANGE getPrevious method    
    def getPrevious(self):
        '''Returns the reference to whatever is previous (either None or a CardNode). No input.'''
        return self.__previous
    
    # DO NOT CHANGE setPrevious method
    def setPrevious(self, newPrevious):
        '''
        Updates the previous reference.
        Input: newPrevious (None or a CardNode) - the object that will come previous
        Returns: None
        '''          
        assert (isinstance(newPrevious, CardNode) or newPrevious == None),\
               'Cannot set next to {}'.format(type(newPrevious))
        self.__previous = newPrevious      
    
    
    def __lt__(self, anotherCardNode):
        '''
        Checks to see if the CardNode instance is less than anotherCardNode,
        based on rank and suit.
        Input: anotherCardNode (CardNode) - the object that will be compared
        Returns: True if CardNode is less than anotherCardNode, False otherwise
        '''
        # TO DO: delete pass and complete the method 
             
        # cannot directly compare them 
        if CardNode.VALID_RANKS.index(self.getRank()) < CardNode.VALID_RANKS.index(anotherCardNode.getRank()) and\
            CardNode.VALID_SUITS.index(self.getSuit()) < CardNode.VALID_SUITS.index(anotherCardNode.getSuit()):
            return True
        else:
            return False
    
    def __gt__(self, anotherCardNode):
        '''
        Checks to see if the CardNode instance is greater than anotherCardNode,
        based on rank and suit.
        Input: anotherCardNode (CardNode) - the object that will be compared
        Returns: True if CardNode is greater than anotherCardNode, False otherwise
        '''        
        # TO DO: delete pass and complete the method
        
        if CardNode.VALID_RANKS.index(self.getRank()) > CardNode.VALID_RANKS.index(anotherCardNode.getRank()) and\
            CardNode.VALID_SUITS.index(self.getSuit()) > CardNode.VALID_SUITS.index(anotherCardNode.getSuit()):
            return True
        else:
            return False        
    
    def isPreviousRank(self, anotherCardNode):
        '''
        Checks to see if the CardNode instance is one less than anotherCardNode,
        based on rank.
        Input: anotherCardNode (CardNode) - the object that will be compared
        Returns: True if CardNode is one less than anotherCardNode, False otherwise
        '''           
        # TO DO: delete pass and complete the method
        if CardNode.VALID_RANKS.index(self.getRank()) + 1 == CardNode.VALID_RANKS.index(anotherCardNode.getRank()) and\
            CardNode.VALID_SUITS.index(self.getSuit()) == CardNode.VALID_SUITS.index(anotherCardNode.getSuit()): 
            return True
        else:
            return False
        
    
    # DO NOT CHANGE __str__ method         
    def __str__(self):
        '''
        If face up, a string showing the rank and suit of the card will be returned.
        If face down, a string showing the back of the card will be returned.
        Input: N/A
        Returns: string representation of the CardNode
        '''
        s = '['
        if self.__faceUp:
            s += ' ' + self.__rank + self.__suit
        s += ' ]'
        return s


class CardList():
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the CardList, which is very similar to a Doubly Linked List.
        A CardList can only have CardNodes and None in its sequence.
        Input: N/A
        Returns: None
        '''
        self.__head = None  # do not change
        self.__tail = None  # do not change
        self.__size = 0     # do not change
    
    # DO NOT CHANGE getHead method     
    def getHead(self):
        '''Returns head of list (either a CardNode or None). No input.'''
        return self.__head
    
    # DO NOT CHANGE getTail method
    def getTail(self):
        '''Returns tail of list (either a CardNode or None). No input.'''
        return self.__tail
    
    # DO NOT CHANGE getSize method
    def getSize(self):
        '''Returns number of CardNodes in sequence. No input.'''
        return self.__size    
    
    # DO NOT CHANGE add method
    def add(self, cardNode):
        '''
        Adds a CardNode to the beginning (head) of the CardList and updates the size.
        Notice the similarity between this and the Doubly Linked List add method.
        Input: cardNode (must be a CardNode)
        Returns: None
        '''
        temp = cardNode
        temp.setPrevious(None) #make sure node is on its own
        temp.setNext(None)     #make sure node is on its own   
        temp.setNext(self.__head)
        if self.__head != None:  # there is a head
            self.__head.setPrevious(temp)
        else:                    # adding to empty list
            self.__tail=temp
        self.__head = temp
        self.__size += 1

    # DO NOT CHANGE append method
    def append(self, cardNode):
        '''
        Appends a CardNode to the end (tail) of the CardList and updates the size.
        Notice the similarity between this and the Doubly Linked List append method.
        Input: cardNode (must be a CardNode)
        Returns: None
        '''        
        temp = cardNode
        temp.setPrevious(None) #make sure node is on its own
        temp.setNext(None)     #make sure node is on its own
        if (self.__head == None):
            self.__head=temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail=temp
        self.__size +=1  
    
     
    def pop(self):
        #TO DO: delete pass and complete method
        pass
    
    
    def sort(self):
        #TO DO: delete pass and complete insertion sort
        pass    
    
      
    def __str__(self):
        #TO DO: delete pass and complete method
        pass
    


class CardStack():
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the CardStack, which is essentially a linked Stack.
        Input: N/A
        Returns: None
        '''        
        self.__cards = CardList()  # do not change
    
    def push(self, card):
        #TO DO: delete pass and complete method
        pass
    
    def pop(self):
        #TO DO: delete pass and complete method
        pass
    
    def peak(self):
        #TO DO: delete pass and complete method
        pass   
    
    def isEmpty(self):
        #TO DO: delete pass and complete method
        pass
    
    def __str__(self):
        #TO DO: delete pass and complete method
        pass
    

   
class Table:
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the Solitaire table. On the table, we will have 1 deck of cards, 
        1 playing pile, 4 foundation piles, and the 7 columns of cards.
        Input: N/A
        Returns: None
        '''
        NUM_COLUMNS = 7
        self.__deck = CardList()        # do not change
        self.__playingPile = CardList() # do not change
        self.__clubs = CardStack()      # do not change
        self.__hearts = CardStack()     # do not change
        self.__spades = CardStack()     # do not change
        self.__diamonds = CardStack()   # do not change
                
        self.__columns = []
        for col in range(NUM_COLUMNS):
            self.__columns.append(CardList())  # do not change      
     
    # DO NOT CHANGE populateDeck method 
    def populateDeck(self, filename):
        '''
        Adds cards to deck based on information in provided text file. We can assume that if
        we can read from the text file, it contains information for a complete and valid deck.
        Input: filename (str) - name of text file
        Returns: None
        '''
        # Important assumption in this implementation: 
        # the top of the deck is at the tail of our CardList
        
        fin = open(filename, 'r')
        for line in fin:
            cardStr = line.strip()
            self.__deck.add(CardNode(cardStr[0], cardStr[1], False)) 
        fin.close()
    
    def rigGame(self):
        #TO DO: delete pass and complete method
        pass
	
    def dealGame(self):
        #TO DO: delete pass and complete method
        pass
    
    def drawThree(self):
        #TO DO: delete pass and complete method
        pass           
   
    def playPileToFoundation(self):
        #TO DO: delete pass and complete method
        pass
    
    def columnToFoundation(self, fromIndex):
        #TO DO: delete pass and complete method
        pass
    
    def displayTable(self):
        #TO DO: delete pass and complete method
        pass
        
    def gameWon(self):
        #TO DO: delete pass and complete method
        pass


################################
## Functions to Test classes  ##
################################
def testCardNode():
    card1 = CardNode('A', 'h')
    print(card1)
    # write additional tests here
    
def testCardList():
    card1 = CardNode('A', 'h')   
    deck = CardList()
    deck.add(card1)
    # write additional tests here
    
def testCardStack():
    stack = CardStack()
    card1 = CardNode('A', 'h')
    stack.push(card1)
    # write additional tests here
    
def testTable():
    table = Table()
    # write tests here
    
    
if __name__ == '__main__':
    # comment/uncomment tests as required.  You may add more tests in any format.
    
    testCardNode()
    #testCardList()
    #testCardStack()
    #testTable()
    
    card2 = CardNode('4', 's')
    card3 = CardNode('A', 'd')
    less = card3 < card2
    more = card2 < card3
    print(less, more)