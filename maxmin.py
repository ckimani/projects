def find_max_min(list):
	min = list[0]
	max = len(list)-1
	
	new_list = []
	for numbs in list:
		if type(numbs) == int:
			list. sort()
			del list[1:-1] 
			return list
			if min == max:
				new_list.append(list)
			return new_list
			
			
		
print(find_max_min([5, 9, -3, 90, 208, 5, 5]))

