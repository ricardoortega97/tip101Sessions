#Problem 1: Nested Constructors

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

#Prints the linked list for string
def printLL(head):
  current = head 
  values = []

  while current:
    values.append(current.value)
    current = current.next
  print("->".join(values))
#Find Fequency 
def countElement(head, val):
  current = head 
  count = 0

  while current:
    if current.value == val:
      count += 1
    current = current.next #proceeds to the next value 

  return count
# Helper function to print the linked list regardless of str/int elem 
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
  # Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        print(f"Current Node: {current.value} -> Next Node: {current.next.value}")
        current = current.next
    print(f"Removing tail node with value: {current.next.value}")
    current.next = None # Remove the last node by setting second-to-last node to None
    return head
#two point technique
def findMiddleElem(head):
  fast = slow = head 

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next #moves by two 

  return slow.value

#palindrome checker
def isPalindromeNode(head):
  if head is None or head.next is None:
    return True 

  #find middle of the list 
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  #reverse the second half of the list 
  prev = None
  while slow:
    nextNode = slow.next
    slow.next = prev
    prev = slow
    slow = nextNode
    # a -> b 

  left, right = head, prev # a -> b | a -> b
  while right:
    if left.value != right.value:
      return False
    left = left.next
    right = right.next

  return True 

#Put it in reverse 
def reverse(head):
  current = head 
  previous = None #new head of the reverse list 
  while current:
    nextNode = current.next #temp stores the next node
    current.next = previous #reverse the current node's pointer
    previous = current #move point by one
    current = nextNode #continue to next node 

  print_list(previous)

#Nested Contructor 
num1 = Node(4, Node(3, Node(5, Node(2, Node(1)))))
head = Node('a', Node('b', Node('c', Node('d'))))
#Finds the Fequency of the input value 
#print(countElement(num1, 3))

#remove_tail(num1)

#print_list(num1)

#print(findMiddleElem(num1))

#print(isPalindromeNode(head))

reverse(head)