from blackjack import deck


def test_draw_card():
    cd = deck.Deck()
    assert cd.size() == 52
    cd.draw()
    assert cd.size() == 51


def test_draw_53_cards():
    cd = deck.Deck()
    for x in range(0, 52):
        cd.draw()
    assert cd.size() == 0
    assert cd.draw() == None

