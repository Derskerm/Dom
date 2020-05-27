import random

class dominion:

	kingdom : Dict[str, deck]
	trash : deck
	
	def __init__(self,kingdom):
		self.kingdom = {}
		self.kingdom[“province”] = deck([card(“province”,”v”,8,victory=6)]*8)
		self.kingdom[“duchy”] = deck([card(“duchy”,”v”,5,victory=3)]*8)
		self.kingdom[“estate”] = deck([card(“estate”,”v”,2,victory=1)]*12)
		self.kingdom[“curse”] = deck([card(“curse”,”c”,0,victory=-1)]*8)
		self.kingdom[“gold”] = deck([card(“gold”,”t”,6,treasure=3)]*30)
		self.kingdom[“silver”] = deck([card(“silver”,”t”,3,treasure=2)]*40)
		self.kingdom[“copper”] = deck([card(“copper”,”t”,0,treasure=1)]*60)
		for card in kingdom:
			self.kingdom[card.name] = deck([card]*10)
		
	def turn(self, board_state, player):  # move forward one state
		while player.actions > 0:
			action = player.pick_next_action(player.hand)
			self.evaluate_action(action, board_state, player)
		while player.buys > 0:
		buy = player.pick_next_buy()
		player.discard.topdeck(self.kingdom[buy].draw())

	
	def evaluate_action(self, action, board_state, player):
		a_CATB = action_card.evaluate(player.hand)
		player.deck.draw(a_CATB[“cards”])
		player.actions = player.actions + a_CATB[“actions”]
		player.treasure = player.treasure + a_CATB[“treasure”]
		player.buys = player.buys + a_CATB[“buys”]

	
class player:  # B)

	deck : deck
	discard : deck
	cards : deck
	hand : deck
	victory : int
	actions : int
	buys : int
	treasure : int
	
	def __init__(self, cards):
		self.cards = deck(cards)
		self.deck = deck(self.cards)
		self.hand = deck(deck.draw(5))
		self.discard = deck([])
		self.actions = 1
		self.buys = 1
		self.treasure = 0

	def end_turn(self):
		self.discard.topdeck(hand)
		self.cards = deck(self.deck.cards + self.discard.cards)
		self.victory = sum([c.victory for c in self,cards.get_by_type(‘cv’)])
		self.actions = 1
		self.buys = 1
		self.treasure = 0
		self.draw(5)
###
		if len(self.deck) >= 5:
			self.hand = deck(self.deck.draw(5))
			if len(self.deck) == 0:
				self.discard.shuffle()
				self.deck = self.discard
				self.discard = deck()
		else:
			self.hand = deck(self.deck.draw(len(self.deck)))
			self.discard.shuffle()
			self.deck = self.discard
			self.discard = deck([])
			self.hand.topdeck(self.deck.draw(5-len(self.hand)))
###

	def draw(self,count=1):
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
		map[“cards”] = len(cards)
		map[“actions”] = actions
		map[“treasure”] = treasure
		map[“buys”] = buys
		return map


	def pick_next_action(self, CATB): 
		if self.actions == 0:
			return None
		best_action = None
		best_reward = 0
		for action_card in hand.get_by_type(‘a’):
			a_CATB = action_card.evaluate(hand)
			a_reward = imitation_heuristic(action_card, a_CATB)
			if a_reward > best_reward or best_reward == 0:
				best_action = action_card
				best_reward = a_reward
		return best_action

def pick_next_buy(self, kingdom):
	CATB = get_CATB()
buy_priority_list = generate_buy_priority_list()
index = 0

	if CATB[“treasure”] >= 8:
		index = 0
	elif CATB[“treasure”] >= 6:
		index = 1
	elif CATB[“treasure”] == 5: #and turns > 15:
		index = 2
	elif CATB[“treasure”] >= 3:
		index = 3
	elif CATB[“treasure”] == 2: #and turns > 15:
		index = 4
	while len(kingdom[buy_priority_list[index]]) == 0:
		index += 1

	def generate_buy_priority_list(self):
		return [“province”, “gold”, “duchy”, “silver”, “estate”]

def imitation_heuristic(self, card, CATB):
	card_heur = math.log(CATB[“cards”] * 4 + 1)
action_heur = math.log(CATB[“actions”] * 5 + 1)
	treasure_heur = 0 if CATB[“treasure”] < 2 else 2 if CATB[“treasure”] < 5 else 4 if CATB[“treasure”] < 8 else 6
	buy_heur = math.log(CATB[“buys”] + 1)
	return card_heur + action_heur + treasure_heur + buy_heur + 2 if card.has_effect()


class deck:
	
	cards : List[card]

	def __init__(self, cards=[]):
		self.cards = []
		for card in cards:
			self.cards.append(card)
		self.shuffle()

	def __len__(self)
		return len(cards)

	def shuffle(self):
		random.shuffle(self.cards)

	def draw(self,count=1):
		if count < 0:
			throw ValueError(“Cannot draw negative cards”)
		if count > len(self):
			throw ValueError(“Cannot draw more than the deck”)
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
		elif type(card) is List[card]:
			self.cards += card

	def is_empty(self):
		return len(cards) == 0

	def get_by_type(self,type,exact_match=False):
		type = type.sorted()
		my_cards : List[card] = []
		for card in self.cards:
			if type==card.type:
				my_cards.append(card)
			elif not exact_match:
				for x in type:
if x in card.type:
	my_cards.append(card)
	break
	
	
class card:
	
	type : str
	actions : int
	buys : int
	cards : int
	treasure : int
	victory : int
	cost : int
	name : str

	def __init__(self,name,type,cost,actions=0,buys=0,cards=0,treasure=0,victory=0, player_fn = lambda player : return, opponent_fn = lambda opponent : return):
		self.name = name
		self.type = type.sorted()
		self.cost = cost
		self.actions = actions
		self.buys = buys
		self.cards = cards
		self.treasure = treasure
		self.victory = victory
		self.player_fn = player_fn
		self.opponent_fn = opponent_fn

	def dup(self):
		return card(self.name, self.type, self.cost, self.actions, self.buys, self.cards, self.treasure, self.victory, self.player_fn, self.opponent_fn)

	def play(self,player,opponents):
		self.player_fn(player)
		for opponent in opponents:
		self.opponent_fn(opponent)
