def max_min(list):
	new_list=[]
	max=list[0]
	min=list[0]
	for numb in list:
		if numb>max:
			max=numb
			return max
		elif numb<min:
			min=numb
			return min
		else:
			if numb==max and numb==min:
				new_list.append(numb)
			return new_list
print(max_min([18,-8,9,78]))