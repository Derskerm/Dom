from dominion import dominion
from card import card
from player import player

def main():
    village = card("village",'a',3,2,0,1,0,0)
    my_dom = dominion([village] * 10)
    copper = card("copper", "t", 0, treasure=1)
    estate = card("estate","v",2,victory=1)
    my_player = player([copper] * 7 + [estate] * 3)
    my_dom.turn(None,my_player)

if __name__ == "__main__":
    main()