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