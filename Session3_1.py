#Calling Mississippi
def count_mississippi(limit):
  for num in range(1, limit + 1):
    print( f"{num} mississippi")

count_mississippi(5)

#Swap Ends
def swap_ends(my_str):
  '''Grabs the last element, excludes the first element[0] and the last[-1],
  grabs the first element '''
  new_str = my_str[-1] + my_str[1:-1] + my_str[0]

  return new_str 

my_str = "boast"
swapped = swap_ends(my_str)
print(swapped)