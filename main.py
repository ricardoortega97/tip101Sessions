'''class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage 
    # The amount of damage this pokemon does to its opponent every attack

  def attack(self, opponent):
    opponent.hp = opponent.hp - self.damage
    print(f"{self.name} dealt {self.damage} damage to {opponent.name}!")
    
    if opponent.hp <= 0:
      print(f"{opponent.name} fainted")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 15, 30) 

opponent = bulbasaur
pikachu.attack(opponent)
'''


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def add_first(head, new_node):
  new_node.next = head
  return new_node

def get_tail(head):
  if head is None:
    return None
  current = head
  while current.next is not None:
    current = current.next
  return current.value

def ll_replace(head, original, replacement):
  current = head
  values = []
  while current is not None:
    if current.value == original:
      current.value = replacement
    values.append(current.value)
    current = current.next
  
  for node in values:
    print(node, end = '->')


num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)

head = num1
ll_replace(head, 5, "banana")



'''
num1 = Node("num1")
num2 = Node("num2")
num1.next = num2
num3 = Node("num3")
num2.next = num3
head = num1
tail = get_tail(num1)
print(tail)


node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)
node_1.next = node_2
nu
node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
'''

