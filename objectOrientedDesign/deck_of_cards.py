import random
from enum import Enum

class Suit(Enum):
    club = 0
    diamond = 1
    heart = 2
    spade = 3

class Card():
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit

class Deck():
    """
        A data structure for a generic deck of cards (standard 52 cards).
    """
    def __init__(self, cards):
        self.cards = cards
        self.nextCard = 0
        self.size = len(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_next_card(self):
        if self.size <= self.nextCard:
            self.nextCard = 0
        val = self.cards[self.nextCard]
        self.nextCard += 1
        return val
