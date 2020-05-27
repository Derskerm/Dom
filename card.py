class card:

    def __init__(self,name,kind,cost,actions=0,buys=0,cards=0,treasure=0,victory=0, player_fn = lambda player : None, opponent_fn = lambda opponent : None):
        self.name : str = name
        self.kind : str = sorted(kind)
        self.cost : int = cost
        self.actions : int = actions
        self.buys : int = buys
        self.cards : int = cards
        self.treasure : int = treasure
        self.victory : int = victory
        self.player_fn = player_fn
        self.opponent_fn = opponent_fn

    def dup(self):
        return card(self.name, self.kind, self.cost, self.actions, self.buys, self.cards, self.treasure, self.victory, self.player_fn, self.opponent_fn)

    def play(self,player,opponents):
        self.player_fn(player)
        for opponent in opponents:
            self.opponent_fn(opponent)