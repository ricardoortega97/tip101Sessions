#Cast vote
def cast_vote(votes, candidate):
    if candidate in votes:
      votes[candidate] = votes[candidate] + 1
    else:
          votes[candidate] = 1
    return votes


votes = {"Alice": 5, "Bob": 3}
print(votes)
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
cast_vote(votes, "Gina")
print(votes)

#Key in common 
def common_keys(dict1, dict2):
  common = []
  for keys in dict1:
    if keys in dict2:
       common.append(keys)
  return common

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

#Highest Prority Task 
def get_highest_priority_task(tasks):

  highest_priority = max(tasks.values())
  highest_task = None
  for task, priority in tasks.items():
    if priority == highest_priority:
      #if highest_task is None or task < highest_task:
        highest_task = task

  tasks.pop(highest_task)
  return highest_task

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
perform_task = (get_highest_priority_task(tasks))
print(perform_task)
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)

#Frequency Count 
def count_occurrences(nums):
  dict = {}

  for i in nums:
    if i not in dict:
      dict[i] = 1
    else: 
      dict[i] = dict[i] + 1

  return dict

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

#Find Majority Count 
def find_majority_element(elements):
  dict = {}

  size = len(elements)
  majority_element = size/2

  for i in elements:
    if i not in dict:
      dict[i] = 1
    else:
      dict[i] = dict[i] + 1
      
  print(dict)
  #for dict in dict.items():  
  if dict[i] > majority_element:
    return i 
    
  return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))