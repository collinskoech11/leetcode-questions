# Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. 
# Return true if the sum exists and return false if it does not.
def find_sum_of_two(A, val):
  A.sort()
  l = 0
  r = len(A)

  while l < r:
    if l+r < val:
      l+=1;
    elif l+r > val:
      r-=1;
    else:
      return True

  return False;
