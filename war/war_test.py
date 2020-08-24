import pytest
import war as w

# war is a game with one deck of cards, shufffled and split into two equal decks, and a card is revealed from each deck per turn, with the highest value card taking both cards in victory

def test_deck():
    #a deck should have 52 cards, 13 different cards of 4 suits
    d = w.Deck()
    assert len(d.new_deck) == 52

def test_deal():
    # a successfull deal should have the deck split into two equal smaller decks
    d = w.Deck()
    d.deal()

    assert len(d.deck1) == 25
    assert len(d.deck2) == 25

def test_draw():
    # a successful draw would remove a card from each players deck and put it in the respective players hand
    d= w.Deck()
    d.deal()

    #check hand is empty
    assert d.p1_card is None
    assert d.p2_card is None

    d.draw()

    # check removal from deck
    assert len(d.deck1) == 24
    assert len(d.deck2) == 24

    #check if card in hand
    assert d.p1_card is not None
    assert d.p2_card is not None
    
def test_reveal():
    # the player with the higher card wins the hand and both cards go to the winners deck
    d = w.Deck()
    d.deal()
    d.draw()
    d.reveal()

    assert len(d.deck1) == 26 and len(d.deck2) == 24
    assert len(d.deck2) == 26 and len(d.deck1) == 24

