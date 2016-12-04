def find_missing(a, b):
	for n in a and b:
		if type(n)==list:
			if len(a)==0 and len(b)==0:
				return 0
			elif len(a)==len(b) and n in a==n in b:
				return [0]*2
			else:
				if len(a)>len(b):
					return (n for n in a if n not in b)
				else:
					return (n for n in b if n not in b)
	

print (find_missing([1,2,3],[1,2, 6 ,3]))




