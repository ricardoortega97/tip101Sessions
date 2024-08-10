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
print('\n --- Problem 1.4 ---')
#count Rotations 
def count_rotations(nums):
  low, high = 0, len(nums) -1
  while low <= high:
    if nums[low] <= nums[high]:
      return low 
    mid = (low + high) // 2
    next_index = (mid + 1) % len(nums)
    prev_index = (mid -1 + len(nums)) % len(nums)

    if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
      return mid
    elif nums[mid] > nums[high]:
      low = mid + 1
    else:
      high = mid - 1

  return 0 

nums = [11, 12, 15, 18, 2, 5, 6, 8]
output = count_rotations(nums)
print(output) 
print('\n --- Problem 1.5 ---')
#Merge Sort 
def merge(left, right):
    result = [] # List to store the merged result
    i = j = 0 # Pointers to iterate over left and right input arrays

    # Compare elements from left and right halves of the list and add them to the
    # result list in the correct order
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
          result.append(left[i])
          i += 1
      else:
          result.append(right[j])
          j += 1
    # Add any remaining elements from the left half to the result list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right half to the result list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(lst):
  #if the list is empty or less than one 
  if len(lst) <= 1:
    return lst 

  mid = len(lst) // 2
  left_half = lst[:mid]
  right_half = lst[mid:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)

lst = [5,3,4,2,1]
output = merge_sort(lst)
print(output)
print('\n --- Problem 1.6 ---')
#Circle Search
def cir_search(arr, target):
  low, high = 0, len(arr) - 1

  while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
      return mid

    if arr[low] <= arr[mid]:
      if arr[low] <= target < arr[mid]:
        high = mid -1

      else:
        low = mid + 1
    else:
      if arr[mid] < target <= arr[high]:
        low = mid + 1
      else:
        high = mid - 1

  return -1 

nums = [8, 9, 10, 2, 5, 6]
target = 10
print(cir_search(nums, target))
