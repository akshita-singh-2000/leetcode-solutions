def contains_duplicate(input)-> bool:
  # if using set is allowed
  '''
  if len(input)==len(set(input)):
    return True
  else:
    return False
  '''
  temp = []
  for i in range(len(input)):
    if input[i] in temp:
      return True
      break
    else:
      temp.append(input[i])

  return False