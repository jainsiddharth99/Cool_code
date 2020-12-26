# there will be 3 packs fo cards(total 21 cards)
# select one from any one pack
import random
import tkinter
class Card:
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    @property
    def display_value(self):
        named_values = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        return named_values.get(self.value, self.value)

    def __repr__(self):
        return f"{self.display_value} of {self.suit}"


def perform_trick():
    
    deck = [Card(val, suit) for val in range(1, 14) for suit in Card.suits]
    random.shuffle(deck)
    
    packet=deck[:21]
    
    for i in range(3):
        pack1=[]
        pack2=[]
        pack3=[]
        for j in range(0,21,3):
            pack1.insert(0,packet[j])
            pack2.insert(0,packet[j+1])
            pack3.insert(0,packet[j+2])
        packet=[]
        
        print('select a card')
        print('in which pack your card is?')
        print('Stack 1: '+', '.join([str(card) for card in pack1]) + '/n')
        print('Stack 2: '+', '.join([str(card) for card in pack2]) + '/n')
        print('Stack 3: '+', '.join([str(card) for card in pack3]) + '/n')
        
        selection=int(input("Stack number: "))
        packet=collect(selection,pack1,pack2,pack3)
    print('Your card is: %s' % packet[10])
    
def collect(row,*packets):
    
    if row ==1:
        return packets[1]+packets[0]+packets[2]
    elif row ==2:
        return packets[0]+packets[1]+packets[2]
    else:
        return packets[0]+packets[2]+packets[1]
    
perform_trick()
