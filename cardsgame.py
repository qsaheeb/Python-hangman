# Cards Game
from random import shuffle

class Card:
  suits=['spade','heart','diamond','club']

  values=[None,None,'2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

  def __init__(self,su,val):
    """suits + values are ints"""
    self.suit=su
    self.value=val

  def __lt__(self,card2):
    if self.value < card2.value:
      return True
    if self.value == card2.value:
      if self.suit < card2.suit:
        return True
    return False

  def __gt__(self,card2):
    if self.value > card2.value:
      return True
    if self.value == card2.value:
      if self.suit > card2.suit:
        return True
    return False

  def __repr__(self):
    op= self.values[self.value] + " of " + self.suits[self.suit]
    return op



class Player:
  def __init__(self,name):
    self.name=name
    self.wins=0
    self.card=None

class Deck:
  def __init__(self):
    self.cards=[]
    for i in range(2,15):
      for j in range(0,4):
        self.cards.append(Card(j,i))

    shuffle(self.cards)

  def remove_card(self):
    if len(self.cards) != 0:
      return self.cards.pop()

class Game:
  def __init__(self):
    self.name1=input("Enter Player 1 name: ")
    self.name2=input("Enter Player 2 name: ")
    self.P1=Player(self.name1)
    self.P2=Player(self.name2)
    self.deck=Deck()

  def draw(self,p1n,p2n,p1c,p2c):
    msg="{} drew {}, {} drew {}.".format(p1n,p1c,p2n,p2c)
    print(msg)

  def wins(self,player):
    print("{} wins this round!".format(player))

  def playgame(self):
    print("Game Begins!")
    cards=self.deck.cards
    while(len(cards) >= 2):
      res=input("Enter any key (Enter 'q' to exit game!): ")
      if res == "q":
        break
      p1c=self.deck.remove_card()
      p2c=self.deck.remove_card()
      self.draw(self.P1.name,self.P2.name,p1c,p2c)
      if p1c > p2c:
        self.P1.wins+=1
        self.wins(self.P1.name)
      else:
        self.P2.wins+=1
        self.wins(self.P2.name)
    

    if len(cards) < 2:
      if self.P1.wins > self.P2.wins:
        self.winner(self.P1.name)
      if self.P1.wins < self.P2.wins:
        self.winner(self.P2.name) 
      else:
        print("\nOh! It was tie!")

  def winner(self,player):
    print("The winner of this game is {}!".format(player))    

game=Game()
game.playgame()
