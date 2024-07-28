#Problem 1 Neattly Nested

'''Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ). Your solution must be recursive.'''

def is_nested(paren_s):
  if paren_s == "":
    return True
  if paren_s[0] == ')' and paren_s[-1] == '(':
    return False

  if  paren_s[0] == '(' and paren_s[-1] == ')':
      return is_nested(paren_s[1:-1])

  return False


s = "(())" #True
s2 = '(()))' #Should be false 
s3 = ""

print(is_nested(s))
print(is_nested(s2))
print(is_nested(s3))
print("--- Problem 2 ---")


'''Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.'''

def count_ones(lst):
  low, high = 0, len(lst) -1 

  while low <= high:
    mid = (high + low) //2


  def binary_search(lst, low, high):
    low = lst[0]
    high = lst[-1]
    if low < high:
      return 0
    mid = (low + high) // 2
    if lst[mid] == 1:
      return (high - mid + 1) 
    else:
      return binary_search(lst, mid + 1, high)





lst = [0, 1, 0, 1, 1, 0]
lst2 = [0, 0]
lst3 = [1]

print(count_ones(lst))
print(count_ones(lst2))
print(count_ones(lst3))