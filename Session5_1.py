# 5.1 Pokemon Class 
class Pokemon:
  def __init__(self, name, types, evolution= None):
      self.name = name
      self.types = types
      self.is_caught = False
      self.evolution = evolution

  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })

  def catch(self):
    self.is_caught = True

  def choose(self):
    if self.is_caught:
      print(f"{self.name} is wild! Catch them if you can!")
    else:
      print(f"{self.name} I choose you! ")

  def add_type(self, new_type):
    self.types.append(new_type)

  def __repr__(self) -> str:
    return self.name

def getByType(myPokemon, pokemonType):
    haveType = []
    for pokemon in myPokemon:
      if pokemonType in pokemon.types:
        haveType.append(pokemon)

    return haveType

def get_evolutionary_line(starter_pokemon):
  evolution = [starter_pokemon]

  currentPokemon = starter_pokemon
  while currentPokemon.evolution:
    evolution.append(currentPokemon.evolution)
    currentPokemon = currentPokemon.evolution

  return evolution

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)


'''my_pokemon = Pokemon('pikachu', ["Electric"] )
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.print_pokemon()
squirtle.is_caught = True

squirtle.print_pokemon()

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()

jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])


myPokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = getByType(myPokemon, "Normal")
print(normal_pokemon)'''

#Understanding Node
class Node:
  def __init__(self, value, next=None) -> None:
    self.value = value
    self.next = next



nodeOne = Node('a')
nodeTwo = Node('b')
nodeOne.next = nodeTwo #linking the node as nodeOne's next property 
print(nodeOne.value)
print(nodeOne.next.value)
print(nodeTwo.value)

#Mario Party 

node_1 = Node('Mario')
node_2 = Node('Luigi')
node_1.next = node_2
node_3 = Node("Wario")
node_2.next = node_3
node_4 = Node("Toad")
node_3.next = node_4


print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

#Linked list 


def print_linked_list(head):
  current = head 
  values = []
  while current:
    values.append(current.value)
    current = current.next
  print("->".join(values))


a = Node('a')
b = Node('b')
a.next = b
c = Node("c")
b.next = c
d = Node('d')
c.next = d
e = Node('e')
d.next = e

print_linked_list(a)

#Card class
class Card():
  def  __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    self.card = []

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

my_card = Card("Hearts", "7")
#print(my_card.isValid())
print(my_card.getValue())
card_two = Card("Spades", "Jack")
print(card_two.getValue())
#second_draw = Card("Spades", "Joker")
#print(second_draw.isValid())

'''card = Card("Spades", "8")
  card = Card("Clubs", "Ace")
  card.suit = "Hearts"
  card.printCard()'''
