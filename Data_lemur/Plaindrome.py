def isPalindrome(phrase):

  left = 0
  right = len(phrase)-1
  
  while left < right:
    # skip over non-alphanumeric
    if not phrase[left].isalnum():
      left = left+1
      continue
    if not phrase[right].isalnum():
      right = right-1
      continue
    
    if phrase[left].lower() == phrase[right].lower():  
      left = left+1
      right = right-1
    else:
      return False
  
  return True