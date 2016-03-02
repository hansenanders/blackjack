import random

def calc_score(hand):
    def get_value(v):
        if v > 10 and v < 14:
            return 10
        elif v == 14:
            return 11
        else:
            return v

    retval = 0
    aces = 0
    for card in hand:
        v = get_value(card)
        retval += v
        if v == 11:
            aces += 1
    if  retval > 21 and aces != 0:
        retval -= 10*aces
    return retval

JACK = 11
QUEEN = 12
KING = 13
ACE = 14

def print_hand(hand):
    def cov(v):
        if v is JACK:
            return 'J'
        elif v is QUEEN:
            return 'Q'
        elif v is KING:
            return 'K'
        elif v is ACE:
            return 'A'
        else:
            return v

    d_hand = [cov(c) for c in hand['dealer']]
    p_hand = [cov(c) for c in hand['player']]
    print('Dealer: %s / %s' % (d_hand, calc_score(hand['dealer'])))
    print
    print('You have: %s / %s' % (p_hand, calc_score(hand['player'])))


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


