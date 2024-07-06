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