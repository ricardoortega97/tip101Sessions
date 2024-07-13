class Card():
  def  __init__(self, suit, rank, next=None):
    self.suit = suit
    self.rank = rank
    self.next = next

  def printCard(self):
    print(f"{self.rank} of {self.suit}")
#Ensure that the card is valid 
  def isValid(self):
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    if self.suit in suits and self.rank in ranks:
      return True

    return False
#get the value of the unique card 
  def getValue(self):
    if self.rank == 'Ace':
      self.rank = '1'
    elif self.rank == 'Jack':
      self.rank = '11'
    elif self.rank == 'Queen':
      self.rank = '12'
    elif self.rank == 'King':
      self.rank = '13'

    return self.rank

#Hand Class
class Hand:
  def __init__(self):
      self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def remove_card(self, card):
    self.cards.remove(card)

#Suns up the total of the cards values 
def sumHand(hand):
  total = 0
  for card in hand.cards:
    total += int(card.getValue())
  return total
#print the cards of the hand 
def printHand(startingCard):
  cards = []
  current = startingCard
  while current:
    cards.append(current)
    current = current.next

  return cards

card_one = Card("Hearts", "3")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "King")

card_one.next = card_two
card_two.next = card_three

print(printHand(card_one))

'''
card_one = Card("Hearts", "3")
card_two = Card("Hearts", "Jack")
card_three = Card("Spades", "3")

hand = Hand()
hand.add_card(card_one)
hand.add_card(card_two)
hand.add_card(card_three)

sum = sumHand(hand)
print(sum)

my_card = Card("Hearts", "7")
#print(my_card.isValid())
print(my_card.getValue())
card_two = Card("Spades", "Jack")
print(card_two.getValue())
#second_draw = Card("Spades", "Joker")
#print(second_draw.isValid())

card = Card("Spades", "8")
  card = Card("Clubs", "Ace")
  card.suit = "Hearts"
  card.printCard()'''