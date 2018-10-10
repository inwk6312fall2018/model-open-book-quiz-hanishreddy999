
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Player:

	def __init__(self, name: str):
	        self.hand = []
	        self.name = name

	def __str__(self):
	        return self.name


class Spanish21:

	def __init__(self, players: List[Player]):
        	self.deck = pyCardDeck.Deck(
	     	     cards=generate_deck()*6, #since 6 decks of cards are dealt in spanish 21
            	     name='Spanish21 deck',
                     reshuffle=False))
        	self.players = players
        	self.scores = {}
		print("Created a game with {} players.".format(len(self.players)))	

    

	def play_again(self):
    		again = raw_input("Do you want to play again? (Y/N) : ").lower()
    		if again == "y":
	    	    dealer_hand = []
	            player_hand = []
	            cards=generate_deck()*6
	            game()
    		else:
	    	    print "Bye!"
	            exit()

	def total(hand):
    		total = 0
    		for card in hand:
	    		if card == "J" or card == "Q" or card == "K":
	        		total+= 10
	    	elif card == "A":
	        	if total >= 11: total+= 1
	    	else: total+= 11
	    	else:
	    		total += card
    	return total


	def hit(hand):
		card = deck.pop()
		if card == "J"
		if card == "Q"
		if card == "K"
		if card == "A"
		hand.append(card)
	return hand

	def print_results(dealer_hand, player_hand):
		clear()
		print "The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
		print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))

	def spanish21(dealer_hand, player_hand):
		if total(player_hand) == 21:
			print_results(dealer_hand, player_hand)
			print "Congratulations! You got a Spanish21!\n"
			play_again()
		elif total(dealer_hand) == 21:
			print_results(dealer_hand, player_hand)		
			print "Sorry, you lose. The dealer got a Spanish21.\n"
			play_again()

	def score(dealer_hand, player_hand):
		if total(player_hand) == 21:
			print_results(dealer_hand, player_hand)
			print "Congratulations! You got a Spanish21!\n"
		elif total(dealer_hand) == 21:
			print_results(dealer_hand, player_hand)		
			print "Sorry, you lose. The dealer got a Spanish21.\n"
		elif total(player_hand) > 21:
			print_results(dealer_hand, player_hand)
			print "Sorry. You busted. You lose.\n"
		elif total(dealer_hand) > 21:
			print_results(dealer_hand, player_hand)			   
			print "Dealer busts. You win!\n"
		elif total(player_hand) < total(dealer_hand):
			print_results(dealer_hand, player_hand)
	   		print "Sorry. Your score isn't higher than the dealer. You lose.\n"
		elif total(player_hand) > total(dealer_hand):
			print_results(dealer_hand, player_hand)			   
			print "Congratulations. Your score is higher than the dealer. You win\n"

	def game():
		choice = 0
		clear()
		print "WELCOME TO Spanish21!\n"
		dealer_hand = deal(deck)
		player_hand = deal(deck)
		while choice != "q":
			print "The dealer is showing a " + str(dealer_hand[0])
			print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
			blackjack(dealer_hand, player_hand)
			choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
			clear()
			if choice == "h":
				hit(player_hand)
				while total(dealer_hand) < 17:
					hit(dealer_hand)
				score(dealer_hand, player_hand)
				play_again()
			elif choice == "s":
				while total(dealer_hand) < 17:
					hit(dealer_hand)
				score(dealer_hand, player_hand)
				play_again()
			elif choice == "q":
				print "Bye!"
				exit()
	def game():
	choice = 0
	clear()
	print "WELCOME TO Spanish21!\n"
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	while choice != "q":
		print "The dealer is showing a " + str(dealer_hand[0])
		print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
		spanish21(dealer_hand, player_hand)
		choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
		clear()
		if choice == "h":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "s":
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "q":
			print "Bye!"
			exit()
	
	def generate_deck() -> List[Spanish21]:
	    """
	    Function that generates the deck, instead of writing down 50 cards, we use iteration
	    to generate the cards for use
	
	    :return:    List with all 48 poker playing cards
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
	             #'10': 'Ten', we don't include this 4 cards in spanish 21
	             'J': 'Jack',
	             'Q': 'Queen',
	             'K': 'King'}
	    cards = []
	    for suit in suits:
	        for rank, name in ranks.items():
	            cards.append(Spanish21(suit, rank, name))
	    print('Generated deck of cards for the table')
	    return cards
	
if __name__ == "__main__":
    	game = BlackjackGame([Player("Kit"), Player("Anya"), Player("Iris"),
        	Player("Simon")])
	game.blackjack()
