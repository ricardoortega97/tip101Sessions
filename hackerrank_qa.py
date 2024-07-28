#recursive prediction 
def mysteryFuction(n):
  if n == 0:
    return 0

  if n % 2 == 1: #If odd, then return 2 and call fuction 
    return 2 + mysteryFuction(n-1)
  else:
    return 3 + mysteryFuction(n-1)

output = mysteryFuction(4)

print(output) #output: 3, 2, 3, 2 = 10 


#recursive call

def recursiveFuction(a,b):
  if b < 0:
    return -1 * recursiveFuction(a, -b) 
    #returns the output value to a negative but also converts b to a positive 

  if b == 0:
    return 0
  #adds 3 each call 
  return a + recursiveFuction(a, b - 1) 

output = recursiveFuction(3,-2)

print(output) # 3 + 3 * -1 = -6 