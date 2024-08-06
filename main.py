#In the Stars
print("\n --- Problem 3.1 ---")
def insertStars(s):
    if len(s) <= 1:
      return s

    else:
      return s[0] + "*" + insertStars(s[1:])

output = insertStars('abcd')
print(output)
print("\n --- Problem 3.2 ---")

#String Lenght Cases
def strLength(s):
  if not s:
    return 0

  else:
    return 1 + strLength(s[1:])

output = strLength('abc')
print(output)
print("\n --- Problem 3.3 ---")
#Recursive Digits Sum 
def sumDigits(n):
  if n == 0:
    return 0
  else:
    return (n % 10) + sumDigits(n // 10)


output = sumDigits(12345)
print(output)
print("\n --- Problem 3.4 ---")

#Recursive Count 7s
def countSevens(n):
  if n == 0:
    return 0
  elif n % 10 == 7:
    return 1 + countSevens(n // 10)
  else:
    return countSevens(n // 10)
n = 727
output = countSevens(n)
print(output)
print("\n --- Problem 3.5 ---")

#Binary Search III
def binaryIII(lst, target):
  left, right = 0, len(lst) - 1

  while left < right:
    mid = (left + right) // 2

    if lst[mid] == target:
      return True
    elif lst[mid] > target:
      right = mid -1
    else:
      left = mid + 1

  return False

lst = lst = [1, 3, 5, 7, 9, 11, 13, 15]
output = binaryIII(lst, 11)
print(output)
print("\n --- Problem 3.6 ---")
#Find Missing
def find_missing(nums):
  left, right = 0, len(nums)

  while left < right:
    mid = (left + right) // 2
    if nums[mid] > mid:
      right = mid
    else:
      left = mid + 1
      
  return left 

nums = [0,1,2,3]
output = find_missing(nums)
print(output)
print("\n --- Problem 3.7 ---")
#Square Root 
def sqrt(x):
  if x < 2:
    return X
    
  left, right = 1, x // 2
  while left <= right:
    mid = (left + right) // 2
    mid_sqrt = mid * mid
    if mid_sqrt == x:
      return mid
    elif mid_sqrt < x:
      left = mid + 1
    else:
      right = mid - 1

  return right

print(sqrt(16))
    


  
  

