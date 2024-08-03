def display_pattern(num):
	col = ((num+1)*2)+1
	row = ((num+1)*2)-1
	for i in range((row // 2)+1):
		for j in range(col):
			if (j+i) == col//2 or (j-i) == col//2:
				print("* ", end="")
			elif (j == (row // 2)+1)and(i == (j-1)):
					print(num,"", end="")
			else:
				print("  ", end="")
		print()
	
	for i in range((row // 2)-1, 0, -1):
		for j in range(col):
			if (j+i) == col//2 or (j-i) == col//2:
				print("* ", end="")
			else:
				print("  ", end="")
		print()
	for i in range(num):
		for j in range(col):
			print("* ", end="")
		print()
	


def print_pattern(num):
	if (num < 1):
		return "Enter number greater than 1"
	else:
		tmp = (num -int(num));
		if tmp < 1 and tmp > 0:
			return "Enter +ve Integer value"
			
		return display_pattern(int(num))

for i in range(10):
	print(print_pattern(i))