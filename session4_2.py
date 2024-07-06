#1 long Pressed
def is_long_pressed(name, typed):
  i, j = 0, 0 

  while i < len(name) and j < len(typed):
    if name[i] == typed[j]:
      i += 1
      j += 1
    elif j > 0 and typed[j] == typed[j -1]:
      j += 1
    else: 
      return False
  #print(name[i - 1]) last char in the str 
  if i < len(name):
    return False
  while i > len(typed):
    if typed[j] != name[i -1]:
      print(name[i -1])
      return False
    j += 1
  return True 

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))
name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))
name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

#Sharing Cookies
def findContentChildren(s, g):
  content = 0
  s.sort()
  g.sort()
  i, j = 0, 0
  while i < len(g) and j < len(s):
    if s[j] >= g[i]:
      print(f"child '{i}' has a greed factor of {g[i]}")
      print(f"Cookie '{j}' has the size of {g[i]} --> Content child.")
      content += 1
      i += 1
      j += 1
    elif s[j] < g[i]:
      print(f"child '{i}' has a greed factor of {g[i]}")
      print(f"cookie '{j}' has the size of {s[j]},"+
           " this child will not be content.")
      i += 1
      j += 1

  return content 

g = [1,1]
s = [2,2,2]

print(findContentChildren(s, g), "children are content.")

#3 Valid Palindrome
def isPalindrome(s, left, right):
  while left < right:
    if s[left] != s[right]:
      return False
    left, right = left + 1, right -1
  return True

def validPalindrome(s):
  left, right = 0, len(s) -1

  while left < right:
    if s[left] != s[right]:
      return isPalindrome(s, left + 1, right) or isPalindrome(s, left, right -1)
    left, right = left + 1, right -1

  return True

s = "aba"
s2 = "abca"
s3 = "abc"
print(validPalindrome(s))
print(validPalindrome(s2))
print(validPalindrome(s3))

#4 Positive Negative Pairs
def find_largest_k(nums):
  nums.sort()
  print(nums)
  if 0 in nums:
    return -1

  left, right = 0, len(nums) -1
  largestK = -1

  while left < right:
    sum = nums[left] + nums[right]
    if sum < 0:
      left += 1
    elif sum > 0:
      right -= 1
    else:
      largestK = nums[right]
      left += 1
      right -= 1
  return largestK

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))
nums2 = [-10,2,5,6,-5,7,-3]
print(find_largest_k(nums2))

#5 Good Substring
def count_good_substrings(s):
  occurance = 0

  for i in range(len(s) - 2):
    window = s[i:i+3]
    print(window)
    if len(window) == len(set(window)):
        occurance += 1

  return occurance


s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))

#Duplicates within Range
def contains_nearby_duplicate(lst, k):
  dic = {}

  for i, elem in enumerate(lst):
    print(i, elem)
    if elem in dic and i - dic[elem] <= k:
      return True

    dic[elem] = i 
  return False

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))