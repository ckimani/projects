def find_missing(a, b):
  a = set(a)
  b = set(b)
  if a < b:
    c = list(b-a)
  elif a > b:
  	c = list(a - b)
  else:
  	return [0]*3
  
  for elements in c:
  	return elements
  
	
 
print find_missing((1,2,3,4,5), (1,2,3,4))



