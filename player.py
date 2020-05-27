from deck import deck
from card import card
import math

class player:  # B)
    
    def __init__(self, cards):
        self.cards : deck = deck(cards)
        self.deck : deck = deck(self.cards)
        self.hand : deck = deck(self.deck.draw(5))
        self.discard : deck = deck([])
        self.actions : int = 1
        self.buys : int = 1
        self.treasure: int = 0
        self.victory: int = 0

    def end_turn(self):
        self.discard.topdeck(self.hand)
        self.cards = deck(self.deck.cards + self.discard.cards)
        self.victory = sum(c.victory for c in self.cards.get_by_kind('cv'))
        self.actions = 1
        self.buys = 1
        self.treasure = 0
        self.draw(5)
        return

#        if len(self.deck) >= 5:
#            self.hand = deck(self.deck.draw(5))
#            if len(self.deck) == 0:
#                self.discard.shuffle()
#                self.deck = self.discard
#                self.discard = deck()
#        else:
#            self.hand = deck(self.deck.draw(len(self.deck)))
#            self.discard.shuffle()
#            self.deck = self.discard
#            self.discard = deck([])
#            self.hand.topdeck(self.deck.draw(5-len(self.hand)))

    def draw(self, count=1):
        if count == 0:
            pass
        elif len(self.deck) > count:
            self.hand.topdeck(self.deck.draw(count))
        else:
            my_draw = self.deck.draw(len(self.deck))
            if len(self.discard) == 0:
                self.hand.topdeck(my_draw)
                return
            self.deck = self.discard
            self.deck.shuffle()
            self.discard = deck()
            if len(self.deck) >= count - len(my_draw):
                my_draw += self.deck.draw(count - len(my_draw))
            else:
                my_draw += self.deck.draw(len(self.deck))
                self.hand.topdeck(my_draw)

    def get_CATB(self):
        map = {}
        map["cards"] = len(cards)
        map["actions"] = actions
        map["treasure"] = treasure
        map["buys"] = buys
        return map


    def pick_next_action(self, CATB): 
        if self.actions == 0:
            return None
        best_action = None
        best_reward = 0
        for action_card in self.hand.get_by_kind('a'):
            a_CATB = action_card.evaluate(self.hand)
            a_reward = imitation_heuristic(action_card, a_CATB)
            if a_reward > best_reward or best_reward == 0:
                best_action = action_card
                best_reward = a_reward
        return best_action

    def pick_next_buy(self, kingdom):
        CATB = get_CATB()
        buy_priority_list = generate_buy_priority_list()
        index = 0

        if CATB["treasure"] >= 8:
            index = 0
        elif CATB["treasure"] >= 6:
            index = 1
        elif CATB["treasure"] == 5: #and turns > 15:
            index = 2
        elif CATB["treasure"] >= 3:
            index = 3
        elif CATB["treasure"] == 2: #and turns > 15:
            index = 4
        while len(kingdom[buy_priority_list[index]]) == 0:
            index += 1

        def generate_buy_priority_list(self):
            return ["province", "gold", "duchy", "silver", "estate"]

    def imitation_heuristic(self, card, CATB):
        card_heur = math.log(CATB["cards"] * 4 + 1)
        action_heur = math.log(CATB["actions"] * 5 + 1)
        treasure_heur = 0 if CATB["treasure"] < 2 else 2 if CATB["treasure"] < 5 else 4 if CATB["treasure"] < 8 else 6
        buy_heur = math.log(CATB["buys"] + 1)
        return card_heur + action_heur + treasure_heur + buy_heur + 2 if card.has_effect() else None