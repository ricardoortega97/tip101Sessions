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