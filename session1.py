def counter(stop):
  for x in range(1,stop + 1):
    print(x)

def sum_ten():
  sum = 0
  for i in range(1, 11):
    sum += i
  return sum

def sum_positive_range(stop):
  sum = 0
  for i in range(1, stop + 1):
    sum += i
  return sum

def sum_range(start, stop):
  return sum(range(start, stop + 1))

def print_negatives(lst):
  for i in lst:
    if(i < 0):
      print(i)
  else: 
      pass



counter(6)
print(sum_ten())
print(sum_positive_range(6))
print(sum_range(3,9))
print_negatives([1,-2,3,4,-5])