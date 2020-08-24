import random as r

class Deck:
    def __init__(self):
        self.new_deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
        self.deck1 = []
        self.deck2 = []
        self.p1_card = None
        self.p2_card = None

    def deal(self):
        r.shuffle(self.new_deck)
        self.deck1 = self.new_deck[0:25]
        self.deck2 = self.new_deck[26:51]
        return self.deck1, self.deck2

    def draw(self):
        self.p1_card = self.deck1.pop(1)
        self.p2_card = self.deck2.pop(1)
        return self.p1_card, self.p2_card

    def war(self):
        self.p1_card_facedown = self.deck1.pop(1)
        self.p1_card_faceup = self.deck1.pop(1)
        self.p2_card_facedown = self.deck2.pop(1)
        self.p2_card_faceup = self.deck2.pop(1)

        if self.p1_card_faceup > self.p2_card_faceup:
            self.deck1.append(self.p1_card)
            self.deck1.append(self.p1_card_facedown)
            self.deck1.append(self.p1_card_faceup)
            self.deck1.append(self.p2_card)
            self.deck1.append(self.p2_card_facedown)
            self.deck1.append(self.p2_card_faceup)
        elif self.p1_card_faceup < self.p2_card_faceup:
            self.deck2.append(self.p1_card)
            self.deck2.append(self.p1_card_facedown)
            self.deck2.append(self.p1_card_faceup)
            self.deck2.append(self.p2_card)
            self.deck2.append(self.p2_card_facedown)
            self.deck2.append(self.p2_card_faceup)
        return self.deck1, self.deck2

    def reveal(self):
        if self.p1_card > self.p2_card:
            self.deck1.append(self.p1_card)
            self.deck1.append(self.p2_card)
        elif self.p2_card > self.p1_card:
            self.deck2.append(self.p1_card)
            self.deck2.append(self.p2_card)
        else:
            self.war()
        return self.deck1, self.deck2
        

