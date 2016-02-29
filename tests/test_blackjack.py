from blackjack import blackjack


def test_player():
    hand = [2, 2]
    assert blackjack.calc_score(hand) == 4

def test_player_score_with_jack():
    hand = [11]
    assert blackjack.calc_score(hand) == 10

def test_player_score_with_queen():
    hand = [12]
    assert blackjack.calc_score(hand) == 10

def test_player_score_with_queen():
    hand = [13]
    assert blackjack.calc_score(hand) == 10

def test_player_score_with_one_ace():
    hand = [14]
    assert blackjack.calc_score(hand) == 11

def test_player_score_with_multiple_ace():
    hand = [14, 14]
    assert blackjack.calc_score(hand) == 2


#def test_dummy():
#    bj = blackjack.BlackJack()
#    bj.run()

