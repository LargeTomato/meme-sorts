def QuickBogo(array):
  ### A recursively defined stupid, random bastardisation of quicksort
  ### A galaxy brain divide and conquer optimisation of bogosort
  ### Complexity of O(2^n log(n)), I think?
  import random
  if len(array) == 1: return array
  if len(array) == 0: return []
  while (True):

    ## Randomly sort into two lists ##
    pivot = random.choice(array) #choose random pivot
    array.remove(pivot)
    left = []
    right = []
    for element in array:
      if random.random() < 0.5:
        left = left + [element]
      else:
        right = right + [element]
    #print(pivot)
    #print(left)
    #print(right)

    ## Check if random sorting is correct ##
    leftCheck = 0
    rightCheck = 0
    if(all(left[i] <= pivot for i in range(len(left)))):
      leftCheck = 1
      
    if(all(right[i] >= pivot for i in range(len(right)))):
      rightCheck = 1
      
    if leftCheck * rightCheck == 1:
      break #check both lists to see if left is all below pivot AND right is all above pivot
      print(left, right)

    array.append(pivot)
    #if this line is reached, then this loop failed on this iteration, readd the pivot back to the array

  return QuickBogo(left) + [pivot] + QuickBogo(right) # Only reached if the above break is executed
