import pyCardDeck
from typing import List

class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name


class PokerTable:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck(
            cards=generate_deck(),
            name='Poker deck',
            reshuffle=False)
        self.players = players
        self.table_cards = []
        print("Created a table with {} players".format(len(self.players)))

def Cantrell_Draw(self):
        """
        Basic Five card game structure
        """
        print("Starting a round of Cantrell Draw")
        self.deck.shuffle()
        self.deal_cards(5)
	#Imagine the first round of betting happened here after cards are drawn and visible to player
	self.draw1()
	self.fold() #players who folded the hands after initial cards were distributed
	self.remove()
	self.after_the_draw()
        # Imagine post-turn, pre-draw1 logic for betting here
	self.reset() #to update the players with hands
	self.fold() 
	self.remove()
        self.after_the_draw()
        # Imagine some more betting and winner decision here
	self.cleanup()




def deal_cards(self, number: int):
        """
        Dealer will go through all available players and deal them x number of cards.
        :param number:  How many cards to deal
        :type number:   int
        """
        for _ in range(0, number):
            for player in self.players:
                card = self.deck.draw()
                player.hand.append(card)
                print("Dealt {} to player {}".format(card, player)



def draw1(self,number):
        """
        After the first round of betting, if more than one player exist on the hand or table than a draw occurs where player selects his/her number of cards which he/she wants to replace
        """
        # Burn a card/cards
	if players>1:
		self.number = int(input("how many card/cards you want to replace?"))
        	burned = self.deck.draw()
        	self.deck.discard(burned)
        	print("Burned a card/cards: {}".format(burned))
        	for _ in range(0, number):
            	    card = self.deck.draw()
            	    self.table_cards.append(card)
	    	    print("New card on the table: {}".format(card))

	else:
		print("Game as ended because of only 1 player or no player exists on the table")

def fold(self, player_id):
        if player_id not in self._player_ids:
            raise ValueError("Unknown player id")
        self._folder_ids.add(player_id)

def remove(self, player_id):
        self.fold(player_id)
        self._dead_player_ids.add(player_id)

def reset(self):
	self._folder_ids = set(self._dead_player_ids)



def after_the_draw(self):
        """
        A second "after the draw" betting round occurs beginning with the player to the dealer's left or else beginning with the player who opened the first round (the latter is common when antes are used instead of blinds). This is followed by a showdown
        """

	if players>1:

        	self.5card()
		#check for the highest holding

	else:
		print("only 1 player and the winner is declared")


def cleanup(self):
        """
        Cleans up the table to gather all the cards back
        """
        for player in self.players:
            for card in player.hand:
                self.deck.discard(card)
        for card in self.table_cards:
            self.deck.discard(card)
        self.deck.shuffle_back()
        print("Cleanup done")


def generate_deck() -> List[PokerCard]:
    """
    Function that generates the deck, instead of writing down 50 cards, we use iteration
    to generate the cards for use
    :return:    List with all 50 poker playing cards
    :rtype:     List[PokerCard]
    """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'A': 'Ace',
             '2': 'Two',
             '3': 'Three',
             '4': 'Four',
             '5': 'Five',
             '6': 'Six',
             '7': 'Seven',
             '8': 'Eight',
             '9': 'Nine',
             '10': 'Ten',
             'J': 'Jack',
             'Q': 'Queen',
             'K': 'King'}
    cards = []
    for suit in suits:
        for rank, name in ranks.items():
            cards.append(PokerCard(suit, rank, name))
    print('Generated deck of cards for the table')
    return cards

if __name__ == '__main__':
    table = PokerTable([Player("Jack"), Player("John"), Player("Peter")])
    table.Cantrell_Draw()
