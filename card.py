class card:
    
    type : str
    actions : int
    buys : int
    cards : int
    treasure : int
    victory : int
    cost : int
    name : str

    def __init__(self,name,type,cost,actions=0,buys=0,cards=0,treasure=0,victory=0, player_fn = lambda player : None, opponent_fn = lambda opponent : None):
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