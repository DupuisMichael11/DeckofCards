#Michael Dupuis CIS261 DeckofCards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Deck:
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.reset()
        
    def reset(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        if len(self.deck) == 0:
            return None
        return self.deck.pop()
    
    def count(self):
        return len(self.deck)
    
print("Card Dealer\n")
print("I have shuffled a deck of 52 cards.\n")

deck = Deck()
deck.shuffle()

number_cards_delt = int(input("How many cards woud you like?:  "))
dealt_cards = []

for _ in range(number_cards_delt):
    card = deck.deal()
    if card is not None:
        dealt_cards.append(f"{card.rank} of {card.suit}")
    else:
        print("No more cards in the deck")
        
if dealt_cards:
    print("Here are your cards:\n")
    for card in dealt_cards:
        print(card)
        
cards_remaining = deck.count()
print(f"\nThere are {cards_remaining} cards left in the deck")
print("Good luck!")

        
                        