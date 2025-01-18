def convertToBase13(num):
  if num == 0:
    return "0"
	
  digits = "0123456789ABC"  
  result = ""
  negative = num <0
  num = abs(num)
  
  while num > 0:
    remainder = num % 13
    result = digits[remainder] + result
    num = num // 13
  
  if negative:
    result = '-' + result
    
  return result