#subsequence
def is_subsequence(lst, sequence):
    lstPointer = 0
    sqnPointer = 0
    while(lstPointer < len(lst) and sqnPointer < len(sequence)):
      if sequence[sqnPointer] == lst[lstPointer]:
        sqnPointer = sqnPointer + 1
        if sqnPointer == len(sequence):
          return True
      else:
        lstPointer = lstPointer + 1
        
    return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

#Create Dictionary
def create_dictionary(keys, values):
  dict = {}
  for i in range(len(keys)):
    dict[keys[i]] = values[i]
  print(dict)

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
create_dictionary(keys, values)

#print pairs 
def print_pair(dictionary, target):
  if dictionary.get(target) in dictionary: #if its not in the dictonary 
    print("Key:", target )
    print("Value:", dictionary.get(target)  )
  else:
    print("That pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")