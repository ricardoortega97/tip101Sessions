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

#Is pangram
def is_pangram(my_str):
      alpha = 'abcdefghijklmopqrstuvwxyz'
      dict = {char: 0 for char in alpha}

      my_str = my_str.lower()

      for i in my_str:
        if i in dict:
          dict[i] = dict[i] + 1

      for val in dict.values():
        if val == 0:
          return False 
        else:
          return True 

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))
str2 = "The dog jumped"
print(is_pangram(str2))

#reverse String
def reverse_string(my_str):
  my_str = my_str[::-1]
  return my_str

my_str = "live"
print(reverse_string(my_str))

def first_unique_char(my_str):
  strings = {}
  for char in my_str:
    if char not in strings:
      strings[char] = 1
    else:
      strings[char] += 1

  for index, char in enumerate(my_str):
    if strings[char] == 1:
      return index

  return -1


my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

#Distances 
def min_distance(words, word1, word2):
  index1, index2 = -1, -1
  min_dis = len(words)
  #print("len", min_dis)
  for i, word in enumerate(words):
    if word == word1:
      print(word)
      index1 = i
      if index2 != -1:
        min_dis = min(min_dis, index1 - index2)
    elif word == word2:
        index2 = i 
        if index1 != -1:
          min_dis = min(min_dis, index2 - index1)

  #print("distace" ,min_dis)
  return min_dis if min_dis != len(words) else -1

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)