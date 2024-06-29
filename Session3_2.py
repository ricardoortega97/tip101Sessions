
#Sum of String 
def sum_of_number_strings(nums):
  sum = 0
  for num in nums:
    sum += int(num)

  return sum

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

#remove 
def remove_duplicates(nums):
  count = 1
  while count < len(nums):
    if nums[count] == nums[count -1]:
      nums.pop(count)
    else:
      count += 1

  return nums

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

#Reverse Letters
def reverse_only_letters(s):
  #size of the list
  back = len(s)-1
  newList =[]

  #for loop: 0 to end of list
  for index in range(0,back+1):
  #varibale holds front index and back index
    if(not s[index].isalpha()):
       newList.append(s[index])

    if(s[back].isalpha()):
      newList.append(s[back])

    back -=1

  return newList 
  #return the new list
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

#Longest Uniform Substring
def longest_uniform_substring(s):
  if not s:
      return 0
  max_length = 1
  current_length = 1
  for i in range(1, len(s)):
      if s[i] == s[i-1]:
          current_length += 1
          max_length = max(max_length, current_length)
      else:
          current_length = 1
  return max_length

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

#Teemo attack
def findPoisonedDuration(timeSeries, duration) -> int:
  if not timeSeries:
      return 0
  total = 0 
  #the last one will not next hit to reset the time therefore gets added last 
  for time in range(len(timeSeries) - 1):
      #print(timeSeries[time + 1] - timeSeries[time]) #4 minus 1, 9 minus 4 
      total += min(duration, timeSeries[time + 1] - timeSeries[time])
      #print("total", total )
  return total + duration

timeSeries = [1,4,9,7]
duration = 3

damage = findPoisonedDuration(timeSeries, duration)
print(damage) 

def sumOfUniqueElements(lst1, lst2):  
  unique_sum = 0

  for num in lst1:
      # Count occurrences of num in lst1
      count = 0
      for x in lst1:
          if x == num:
              count += 1

      # Check if num is unique in lst1 and not in lst2
      if count == 1:
          in_lst2 = False
          for y in lst2:
              if y == num:
                  in_lst2 = True
                  break

          if not in_lst2:
              unique_sum += num

  return unique_sum

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7, 1]

sum1 = sumOfUniqueElements(lstA, lstB)
print(sum1)

sum2 = sumOfUniqueElements(lstC, lstB)
print(sum2)