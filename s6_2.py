# Problem 1: Detect Circular Linked List
'''
A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
'''

'''
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def is_circular(head):
  if not head:
    return False

  save = head
  current = head

  while current.next:
    current = current.next
    if current == save:
      return True

  return False



num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
#num3.next = num1

print(is_circular(num1))
'''


# Problem 3 Partition List Around Value
'''
Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.
'''

'''
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def find_last_node_in_cycle(head):
  if not head:
    return False

  slow = fast = head 
  hasCycle = False




num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num4 = Node(4)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num2

print(find_last_node_in_cycle(num1))
'''


# Problem 3: Partition List Around Value
'''
Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

Example Input:

# 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3

Result Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5 or 2 -> 2 -> 1 -> 5 -> 4 -> 3

'''

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def partition(head, val):
  temp_head = Node("temp") 
  temp_head.next = head    

  # Traverse the list
  previous = temp_head
  current = head
  while current:
      if current.value  val:          # If the current node is the node to delete
          previous.next = current.next  # Delete the node
          break                         # Break out of the loop

      previous = current
      current = current.next
  return temp_head.next # Return the head of the input list




lst = Node(1, (Node(4, Node(3, Node(2, Node(5, Node(2) ) ) ) ) ) )
head = 1
val = 3

print(partition(head, val))
#Thanks!
#Nice work today!