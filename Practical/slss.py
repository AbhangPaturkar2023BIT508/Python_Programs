
# def get_sl_ss(list_of_obj)
# -- Second largest num value
# -- Second Smaller num value
# -- can't use builtins
# -- each and every num value (key, value)

def get_num_list(li):
	ans = []
	
	for item in li:
		if isinstance(item, int):
			ans += [item]
		elif isinstance(item, (list, tuple, set)):
			ans += get_num_list(list(item))
		elif isinstance(item, dict):
			item = list(item.keys())+list(item.values())
			ans += get_num_list(item)
			
	return ans
			

def get_sl_ss(obj_list):
	nums_list = get_num_list(obj_list)
	if len(nums_list) == 1 : return -1
	maxi = s_maxi = mini = s_mini =  None
	# print(nums_list)
	
	for val in nums_list:
		#print(val)
		if maxi is None or val >= maxi :
			s_maxi = maxi
			maxi = val
		elif s_maxi is None or val > s_maxi:
			s_maxi = val

		if mini is None or val <= mini:
			s_mini = mini
			mini = val
		elif s_mini is None or val < s_mini:
			s_mini = val

	
	return s_maxi, s_mini
		
	


print(get_sl_ss([11,2,'ab', '4',(3,4,{'g',5}),{'a':10, 5:12}, 14,16,15]))	
print(get_sl_ss([5,4,3,2,1]))
