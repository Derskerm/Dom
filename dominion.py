import math, random
from card import card
from deck import deck
from player import player

class dominion:

    trash : deck
    
    def __init__(self,kingdom):
        self.kingdom : dict[str, deck] = {}
        self.kingdom["province"] = deck([card("province","v",8,victory=6)]*8)
        self.kingdom["duchy"] = deck([card("duchy","v",5,victory=3)]*8)
        self.kingdom["estate"] = deck([card("estate","v",2,victory=1)]*12)
        self.kingdom["curse"] = deck([card("curse","c",0,victory=-1)]*8)
        self.kingdom["gold"] = deck([card("gold","t",6,treasure=3)]*30)
        self.kingdom["silver"] = deck([card("silver","t",3,treasure=2)]*40)
        self.kingdom["copper"] = deck([card("copper","t",0,treasure=1)]*60)
        for c in kingdom:
            self.kingdom[c.name] = deck([c]*10)
        
    def turn(self, board_state, player):  # move forward one state
        while player.actions > 0:
            action = player.pick_next_action(player.hand)
            if action:
                self.evaluate_action(action, board_state, player)
        while player.buys > 0:
            buy = player.pick_next_buy()
            player.discard.topdeck(self.kingdom[buy].draw())

    
    def evaluate_action(self, action, board_state, player):
        a_CATB = {"cards": action.cards, "actions": action.actions, "treasure": action.treasure, "buys": action.buys}
        player.deck.draw(a_CATB["cards"])
        player.actions = player.actions + a_CATB["actions"]
        player.treasure = player.treasure + a_CATB["treasure"]
        player.buys = player.buys + a_CATB["buys"]