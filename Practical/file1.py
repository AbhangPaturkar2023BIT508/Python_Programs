def get_even_odd_count(nums):
	oc = 0
	#ec = 0
	for val in nums:
		oc += (val & 1)
		
		#if (val % 2):
		#	oc+=1
		#else:
		#	ec+=1
	return len(nums)-oc, oc

print(get_even_odd_count([10,20,30,1,-4,3]))


