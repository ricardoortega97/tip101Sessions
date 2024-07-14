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
