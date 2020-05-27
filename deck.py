import random
from card import card

class deck:

    def __init__(self, cards=[]):
        self.cards : list[card] = []
        for card in cards:
            self.cards.append(card)
        self.shuffle()

    def __len__(self):
        return len(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self,count=1):
        if count < 0:
            raise ValueError("Cannot draw negative cards")
        if count > len(self):
            raise ValueError("Cannot draw more than the deck")
        if count == 0:
            return []
        elif count == 1:
            return self.cards.pop()
        my_draw : List[card] = self.cards[len(self.cards)-count:]
        self.cards = self.cards[:len(self.cards)-count]
        return my_draw

    def topdeck(self,card):
        if type(card) is card:
            self.cards.append(card)
        elif type(card) is list[card]:
            self.cards += card

    def is_empty(self):
        return len(cards) == 0

    def get_by_kind(self,kind,exact_match=False):
        kind = kind.sorted()
        my_cards : List[card] = []
        for card in self.cards:
            if kind==card.kind:
                my_cards.append(card)
            elif not exact_match:
                for x in kind:
                    if x in card.kind:
                        my_cards.append(card)
                        break