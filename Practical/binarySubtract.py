def bin_to_deci(num):
	ans = 0
	for digit in num:
		ans = (ans * 2) + (ord(digit) - 48)
	
	return ans
# end of decimal

def binary_subtract(num1, num2):
	max_len = max(len(num1), len(num2))
	num1 = num1.zfill(max_len)
	num2 = num2.zfill(max_len)
	
	is_negative = False
	
	if bin_to_deci(num1) < bin_to_deci(num2):
		is_negative = True
		
	ans = []
	borrow = 0
	
	for i in range(max_len-1, -1, -1):
		dig1 = bin_to_deci(num1[i])
		dig2 = bin_to_deci(num2[i])
		if dig1 >= dig2:
			ans.append(str(dig1 - dig2))
			borrow = 0
		else:
			ans.append(str(dig1+2 - dig2))
			borrow = 1
			
	ans.reverse()
	ans_str = ''.join(ans).lstrip('0')
	
	if ans_str == '':
		ans_str = '0'
		
	if is_negative:
		ans_str = '-' + ans_str
	
	return ans_str

# Example usage
print(f"1010 - 0111 = {binary_subtract('1010', '0111')}")  # Outputs: '0011'
print(f"0111 - 1010 = {binary_subtract('0111', '1010')}")  # Outputs: '-0011'
print(f"1100 - 0011 = {binary_subtract('1100', '0011')}")  # Outputs: '1001'
print(f"0001 - 0001 = {binary_subtract('0001', '0001')}")  # Outputs: '0'
print(f"0000 - 1001 = {binary_subtract('0000', '1001')}")  # Outputs: '-1001' 