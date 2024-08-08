print('\n --- Problem 1.1 ---')
#Neatly Nested 
def isNested(paren):
  #base case: when the list is empty, it is true 
  if paren == '':
    return True

  if paren[0] == "(" and paren[-1] == ')':
    return isNested(paren[1:-1])
  #if the question says that it doesnt mater where the ( ) pairs are along they are pairs then:
  if paren[0] == ")" and paren[-1] == '(':
    return isNested(paren[1:-1])
  #if it doesnt meet up to the end, it will be false
  return False

input = '(()))'
input2 = "(()" # False
print(isNested(input))  
print('\n --- Problem 1.2 ---')
#How many 1s in a O(log n) time 
def count_ones(lst):
  #binary search 
  low, high = 0, len(lst) - 1

  while low <= high:
    mid = (low + high) // 2

    if lst[mid] == 0:
      low = mid + 1
    else:
      high = mid - 1

  if low < len(lst) and lst[low] == 1:
    return len(lst) - low
  return 0 

lst = [0, 0, 1, 0, 1, 1]
print(count_ones(lst))
print('\n --- Problem 1.3 ---')
#Binary Search IV 
def binary_searchIV(nums, left, right, target ):
  if left > right:
    return -1 #The Target is not found

  mid = (left + right) // 2
  #Target found
  if nums[mid] == target:
    return mid
  #move to the left
  if target < nums[mid]:
    return binary_searchIV(nums, left, mid -1, target)
  #move to the right 
  else:
    return binary_searchIV(nums, mid + 1, right, target)
#Recursion helper 
def binary_recursion(nums, target):

  return binary_searchIV(nums, 0, len(nums) -1, target)

input = [1, 3, 5, 11, 7, 0, 13, 15]
print(binary_recursion(input, 0))
 