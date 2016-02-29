from . import deck

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

class BlackJack(object):
    def __init__(self, _deck=None):
        if _deck is None:
            self.deck = deck.Deck()
        else:
            self.deck = _deck

    def run(self):
        player = []
        dealer = []

        player += [self.deck.draw()]
        dealer += [self.deck.draw()]
        player += [self.deck.draw()]

        done = False
        while not done:
#            min(calc_hand_value(player)) <= 17:
            print ("You're hand value: %r" % calc_score(player))
            action = input("h (Hit), s (Stand)")
            if action is 'h':
                player += [self.deck.draw()]
            elif action is 's':
                done = True

            if min(calc_hand_value(player)) > 21:
                print("%s: Busted!!!" % min(calc_hand_value(player)))
                return

        while min(calc_hand_value(dealer)) <= 17:
            dealer += [self.deck.draw()]

        p_value = min(calc_hand_value(player))
        d_value = min(calc_hand_value(dealer))
        print('Player: %s' % p_hand)
        print('Dealer: %s' % d_hand)
        if p_hand <= d_hand:
            print('Dealer wins!')
        else:
            print('Player WINS!!!')

        

def main():
    bj = BlackJack()
    bj.run()

if __name__ == "__main__":
    main()
