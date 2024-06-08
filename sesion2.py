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

