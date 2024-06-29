def is_prime(n):
  #we if not less than 0 
  if n <= 1:
    return False
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1

  return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
#Evaluating Solutions
def reverse_list(lst):
  left_pointer = 0
  right_pointer = len(lst) - 1

  while left_pointer < right_pointer:
    temp = lst[left_pointer]
    lst[left_pointer] = lst[right_pointer]
    lst[right_pointer] = temp

    left_pointer += 1
    right_pointer -= 1

  return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
#More Even Integers
def sort_array_by_parity(nums):
  odd = []
  even = []
  for val in nums:
    print(val)
    if val % 2 == 1:
      odd.append(val)
    if val % 2 == 0:
      even.append(val)

  nums = even + odd
  return nums

nums = [3,5,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))

#Crate another fuction that checks each word if its a palindrome
def isPalindrone(s):
  left, right = 0 , len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True 
 #per each word in the list, it goes into another fuction to determine if it is palidrome
def first_palindrome(words):
  for word in words:
   if isPalindrone(word):
     return word
  return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)
words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)
words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

#Remove duplicates with O(1)
def remove_duplicates(nums):
    if not nums:
        return 0
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j

nums = [1, 1, 2, 3, 4, 4, 4, 5]
print(nums)
new_length = remove_duplicates(nums)
print(new_length)
print(nums[:new_length])

#perfect number 
def is_perfect_number(n):
    sum = 0
    i = 1
    while i <= n // 2:
        if n % i == 0:
            sum += i
        i += 1

    return sum == n

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))

#2-pointer palindrome
def is_palindrome(s):
  left, right = 0, len(s) -1

  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
    print(s[left], s[right])
  return True

s = "amanaplanacanalpanama"
s2 = "hello worlh"

print(is_palindrome(s))
print(is_palindrome(s2))

#Make palindrome
def make_palindrome(s):
  char = list(s)
  left, right = 0, len(s) -1

  while left < right:
    if char[left] != char[right]:
      if char[left] > char[right]:
        char[left] = char[right]
      else:
        char[right] = char[left]      
    left += 1
    right -= 1

  return ''.join(char)

s = "egcfe"
s_pal = make_palindrome(s)
print(s_pal)
s = "abcd"
s_pal = make_palindrome(s)
print(s_pal)

#Reverse Vowels
def isVowel(c):
  return c in "aeiouAEIOU"

def reverse_vowels(s):
  lst = list(s)
  left, right = 0, len(s) - 1

  while left < right:
    while left < right and not isVowel(lst[left]):
      left += 1
    while left < right and not isVowel(lst[right]):
      right -= 1
    temp = lst[left]
    lst[left], lst[right] = lst[right], temp
    left += 1
    right -= 1

  return ''.join(lst)

s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)
s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)

#Two-Pointer Remove Element
def removeElement(nums, val):
  i = 0
  for j in range(len(nums)):
    if nums[j] != val:
      nums[i] = nums[j]
      i += 1


  return i

nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums[:nums_len]) # same list
print(nums_len)