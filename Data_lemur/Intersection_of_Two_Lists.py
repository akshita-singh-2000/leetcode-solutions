def intersection(a, b):
  list1 = []
  
  if len(a)< len(b):
    small_list = a
    big_list = b
  else:
    small_list = b
    big_list = a

  for inx, val in enumerate(small_list):
    if val in big_list:
      list1.append(val)
      
  return list1