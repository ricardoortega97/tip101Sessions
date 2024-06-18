def print_lst(lst):
  for x in lst:
    print(x)

def double(lst1):
  for i in lst1:
    i = i * 2
    print(i)


lst1 = [1,2,3]

print_lst(["squirtle", "gengar", "charizard", "pikachu"])
double(lst1)

#Return Double list 
def doubled(lst1):
  new_lst = []
  for x in lst1:
    new_lst.append(x * 2)
  return new_lst

lst1 = [1,2,3]
new_lst = doubled(lst1)
print(new_lst)

#Flip Signs 
def flip_sign(lst1):
   flipped_lst = []
   for x in lst1:
     flipped_lst.append(x * -1)
   return flipped_lst

lst1 = [1,2,3,4]
flipped_lst = flip_sign(lst1)
print(flipped_lst)

#Max differance 
def max_difference(lst3):
  return (max(lst3) - min(lst3))

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print("Differance between smallest and largest value is:",max_diff)

#Below Threshold
def count_less_than(numbers, threshold):
  counter = 0
  for num in numbers:
    if num < threshold:
      counter += 1
  return counter

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print("Counter:",counter)

#Even List 
def get_evens(lst1):
  evenlst = []
  for i in lst1:
    if i % 2 == 0:
      evenlst.append(i)
  return evenlst

evens_lst = get_evens(lst1)
print(evens_lst)

#Multiple of five 
def multiples_of_five():
  for i in range(1,101):
    if i % 5 == 0:
      print(i)

multiples_of_five()

#Divisors
def find_divisors(n):
  divisors = []
  i = 1
  while i <= n:
    if (n % i == 0):
      divisors.append(i)
    i += 1
  return divisors

lst = find_divisors(10)
print(lst)

#Keys Versus Values
def keys_v_values(dictionary):
  sum_keys = 0
  sum_value = 0
  items = dictionary.items()
  for k, v in items:
    sum_keys = sum_keys + k
    sum_value = sum_value + v

  if sum_keys == sum_value:
    return "Balanced"
  elif sum_keys > sum_value:
    return "Keys"
  else:
    return "Values"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#Restock Inventory
def restock_inventory(current_inventory, restock_list):
  for item, quantity in restock_list.items():
      if item in current_inventory:
          current_inventory[item] += quantity
      else:
          current_inventory[item] = quantity

  return print(current_inventory)

current_inventory = {
"apples": 30,
"bananas": 15,
"oranges": 10
}

restock_list = {
"oranges": 20,
"apples": 10,
"pears": 5
}

restock_inventory(current_inventory, restock_list)

#Calculate gpa
def calculate_gpa(report_card):
  grade_points = {
    "A" : 4, 
    "B" : 3,
    "C" : 2,
    "D" : 1,
    "F" : 0
  }

  total_points = 0
  numOfCourses = 0

  for course, grade in report_card.items():
    total_points += grade_points.get(grade, 0)

    numOfCourses += 1

  if numOfCourses == 0:
    return 0.0

  gpa = total_points/numOfCourses

  return format("%.2f" % gpa)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

#best book
def highest_rating(books):
  if not books:
    pass
  #grabs the element 
  else:
    highest_rating = books[0]
  #for the element in books, narrow down to the sub element 
    for book in books:

      if book["rating"] > highest_rating["rating"]:
        highest_rating = book

    return print(highest_rating)

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
       "author": "Gabrielle Zevin",
       "rating": 4.18
      },
      {"title": "A Fortune For Your Disaster",
       "author": "Hanif Abdurraqib",
       "rating": 4.47
      },
      {"title": "The Seven Husbands of Evenlyn Hugo",
       "author": "Taylor Jenkins Reid",
       "rating": 4.40
      }
]

highest_rating(books)
#problem set 2 
#ndex-Value Map
def index_to_value_map(lst):
  output = {}

  for elem in range(len(lst)):
    output[elem] = lst[elem]

  print(output)

lst = ["apple", "banana", "cherry", "pear"]
index_to_value_map(lst)

#is monotonic 
def is_monotonic(nums):
  increasing = True
  decreasing = True

  for num in range(1, len(nums)):
    if nums[num] < nums[num - 1]:
      #nums4[nums] is 8 and nums4[num - 1] is 9
      increasing = False
    if nums[num] > nums[num - 1]:
      decreasing = False
  #returns if the either variable is true else returns if both false 
  return increasing or decreasing  

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))
nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))
nums3 = [1,1,1]
print(is_monotonic(nums3))
nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))