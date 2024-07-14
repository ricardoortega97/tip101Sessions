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

'''class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def printLinkedLst(head):
  lst = []
  current = head
  while current:
    lst.append(current.value)
    current = current.next
    
  return lst

d = Node('d')
c = Node('c', d)
b = Node('b',c)
a = Node('a', b)

print(printLinkedLst(a))

node1 = Node('aries')
node2  = Node('taurus')
node3 =Node('gemini')
node4 = Node('cancer')
node1.next = node2
node2.next = node3
node3.next = node4

print(node1.value, "->", node1.next.value)
print(node2.value, "->", node2.next.value)
print(node3.value, "->", node3.next.value)
print(node4.value, "->", node4.next)'''

class Player():
  def  __init__(self, character, kart):
    self.character = character
    self.kart = kart
    self.items = []
#Player Character's info
  def getPlayer(self):
      return f"{self.character} driving the {self.kart}"
#Validate the character
  def setPlayer(self, name):
    characters = ['Mario', 'Luigi', 'Peach','Yoshi', 'Toad', 'Wario', 'Donkey Kong', 'Bowser']

    if name in characters:
      self.character = name
      print('Character Updated!')
    else:
      print("Invalid Character")
#Add item to the list
  def addItem(self, itemName):
    itemLst = ['banana', 'green shell', 'red shell', 'blue shell', 'super star', 'lightning', 'bullet bill', 'bob-bomb']

    if itemName in itemLst:
      self.items.append(itemName)

    print(self.items)
#Print the inventory  
  def printInventory(self):
    if not self.items:
      print('Inventory empty')
    else: 
      inventory = {}
      for item in self.items:
        if item in inventory:
          inventory[item] += 1
        else:
          inventory[item] = 1

      inventoryDisplay = ''
      first = True
      for item, count in inventory.items():
        if not first:
          inventoryDisplay += ', '
        inventoryDisplay += f'{item}: {count}'
        first = False

      print(f'Inventory: {inventoryDisplay}')


player_two = Player('Bowser', 'Pieahma Prowler')
player_one = Player('Yoshi', 'Supper Blooper')

#print(player_one.getPlayer())
#print(f'{player_one.getPlayer()} vs {player_two.getPlayer()}')
#update the kart
#player_one.kart = 'Dolphin Dasher'
#print(player_one.getPlayer())
#player_one.setPlayer('Peach')
#player_two.setPlayer('Kermit')

player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.printInventory()
player_two.printInventory()
