#Duplicates within Range
def contains_nearby_duplicate(lst, k):
  dic = {}

  for i, elem in enumerate(lst):
    print(i, elem)
    if elem in dic and i - dic[elem] <= k:
      return True

    dic[elem] = i 
  return False

lst = [1, 2, 3, 1, 2, 3]
lst2 = [1, 0, 1, 1]
print(contains_nearby_duplicate(lst, 2))
print(contains_nearby_duplicate(lst2, 1))