import random

JACK = 11
QUEEN = 12
KING = 13
ACE = 14

class Deck(object):
    '''Standard 52-card deck'''

    def __init__(self):
        self.deck = self.create()

    def create(self):
        new_deck = []
        for i in range(2, 15):
            new_deck += [i for j in range(0, 4)]
        return new_deck

    def shuffle(self):
        self.deck = self.create()

    def draw(self):
        if len(self.deck) == 0:
            return None

        r = random.randint(0, len(self.deck)) - 1
        return self.deck.pop(r)
    
    def size(self):
        s = len(self.deck)
        return s


