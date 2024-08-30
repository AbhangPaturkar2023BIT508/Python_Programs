# def display_pattern(num):
# 	col = ((num+1)*2)+1
# 	row = ((num+1)*2)-1
# 	for i in range((row // 2)+1):
# 		for j in range(col):
# 			if (j+i) == col//2 or (j-i) == col//2:
# 				print("+ ", end="")
# 			else:
# 				print("  ", end="")
# 		print()
	
# 	for i in range((row // 2)-1, -1, -1):
# 		for j in range(col):
# 			if (j+i) == col//2 or (j-i) == col//2:
				
# 				print("+ ", end="")
# 			else:
# 				print("  ", end="")
# 		print()
# 	# for i in range(num):
# 	# 	for j in range(col):
# 	# 		print("* ", end="")
# 	# 	print()
	
def display_pattern1(num):
	size = (num * 2)+1
	for i in range(size):
		if i <= size // 2:
			for j in range(size):
				if ((j+i) == (size // 2) or (j-i) == (size // 2)):
					print("+ ",end="")
				else:
					print("  ", end="")
			print()
		else:
			for j in range(size):
				if ((j + ((size-1) - i)) == (size // 2) or (j - ((size-1) - i)) == (size // 2)):
					if (size - 1) == i:
						print("- ",end="")
					else:
						print("+ ",end="")
				else:
					print("  ", end="")
			print()
			
def display_pattern2(num):
	size = (num * 2)+1
	for i in range(size):
		if i <= size // 2:
			for j in range(size):
				if ((j+i) == (size // 2) or (j-i) == (size // 2)):
					print("+ ",end="")
				else:
					print("  ", end="")
			print()
		else:
			for j in range(size):
				if ((j + ((size-1) - i)) == (size // 2) or (j - ((size-1) - i)) == (size // 2)):
					print("- ",end="")
				else:
					print("  ", end="")
			print()
			
def display_pattern3(num):
	size = (num * 2)+1
	for i in range(size):
		if i % 2 == 0:
			sign = '+'
		else:
			sign = '-'

		if i <= size // 2:
			for j in range(size):
				if ((j+i) == (size // 2) or (j-i) == (size // 2)):
					print(sign," ",end="")
				else:
					print("  ", end="")
			print()
		else:
			for j in range(size):
				if ((j + ((size-1) - i)) == (size // 2) or (j - ((size-1) - i)) == (size // 2)):
					print(sign," ",end="")
				else:
					print("  ", end="")
			print()
		


def print_pattern(num,):
	if (num < 1):
		return "Enter number greater than 1"
	else:
		tmp = (num -int(num));
		if tmp < 1 and tmp > 0:
			return "Enter +ve Integer value"
			
		return display_pattern1(int(num))

# for i in range(10):
print_pattern(5)
print()
display_pattern2(5)
print()
display_pattern3(5)