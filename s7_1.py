def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)

def repeatHelloIterative(n):
  for i in range(n):
    print("Hello +")

#Factorial Cases 
print('\n ---Problem 2 ---')
def factorial(n):
  if n == 0 or n == 1:
    return 1

  return n * factorial(n -1)

output = factorial(5)

print(output)

print('\n --- Problem 3 ---')
#Recursive Sum 
def recursiveSum(lst):
  if len(lst) == 0:
    return 0
  else:
    return lst[0] + recursiveSum(lst[1:])

lst = [1,2,3,4,5]
output = recursiveSum(lst)
print(output)
print('\n --- Problem 4 ---')
#Recursive Power of 2
def is_Pow_of_two(n):
  #Base case
  if n == 1:
    return True
  #Base case 2 if less than one or not divisible by 2 
  elif n < 1 or n % 2 != 0:
    return False

  else:
    return is_Pow_of_two(n // 2)

output = is_Pow_of_two(3)
print(output)
print('\n --- Problem 5 ---')
#Binary Search I Time: 0(log n), Space: 0(1)
def binary(lst, target):
  left, right = 0, len(lst) - 1

  while left <= right:
    mid = (left + right) // 2

    if lst[mid] == target:
      return mid
    elif lst[mid] > target:
      right = mid -1
    else:
      left = mid + 1

  return -1 

lst = [1, 3, 5, 7, 9, 11, 11, 15]
target = 11
output = binary(lst, target)
print(output)
print('\n --- Problem 6 ---')
#Backwards Binary Search 
def findLast(lst, target):
  left, right = 0, len(lst) -1
  var = -1 
  while left <= right:
    mid = (left + right) // 2
    print('mid' , mid)
    if lst[mid] == target:
      var = mid
      left = mid + 1 
    elif lst[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return var 

output = findLast(lst, 11)
print(output)
print('\n --- Problem 7 ---')
#Find Floor Time: 0 (log n), Space: 0(1)
def floor(lst, x):
  low, high = 0, len(lst) -1 
  val = None

  while low <= high:
    mid = (low + high) // 2

    if lst[mid] <= x:
      val = mid
      low = mid + 1
    else:
      high = mid - 1
  return  val 

lst1 = [1, 2, 8, 10, 11, 12, 19]
output = floor(lst1, x = 5)
print(output)
