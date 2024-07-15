class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def chase(head):
  current = head
  values = []
  while current:
    values.append(current.value)
    current = current.next
  print(' chases '.join(values))
    

dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

chase(dog)
