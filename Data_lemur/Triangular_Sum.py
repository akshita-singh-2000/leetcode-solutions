def triangular_sum(nums):
  l=[]
  
  if len(nums)==1: 
    return (nums[0])
    
  elif len(nums)==2: 
    return (nums[0]+nums[1]) % 10
  else:
    for i in range(len(nums)-1):
      l.append((nums[i]+nums[i+1])%10)
      
    return triangular_sum(l)
