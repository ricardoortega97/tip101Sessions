Cast vote
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

#Student Dictory
def student_directory(student_names):
  student_directory = {}
  id_num = 1
  for student in student_names:
    student_directory[student] = id_num
    id_num += 1

  return student_directory

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

print(student_directory(student_names))

#Dictionary Description
def get_description(info, keys):
  for key in keys:
    if key in info:
      print(info[key])
    else:
      print(None)


info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)

#sum evens 
def sum_even_values(dictionary):
  sum = 0 

  for key, value in dictionary.items():
    if value % 2 == 0:
      sum += value
  return sum

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))

#merge catalog
def merge_catalogs(catalog1, catalog2):

  for key, value in catalog2.items():
    if key in catalog1:
      catalog1[key] = value
    else:
      catalog1[key] = value
  print(catalog1)

catalog1 = {"apple": 1.0, "banana": 0.5, "pear" : 2.0}
catalog2 = {"banana": 0.75, "cherry": 1.25}

merge_catalogs(catalog1,catalog2)

#restock items 
def get_items_to_restock(products, restock_threshold):
  low = []
  for key, value in products.items():
    if value < restock_threshold:
      low.append(key)
  return print(low)

products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5

get_items_to_restock(products, restock_threshold)