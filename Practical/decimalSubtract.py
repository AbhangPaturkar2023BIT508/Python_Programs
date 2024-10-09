def decimal(num):
	ans = 0
	for digit in num:
		ans = (ans * 10) + (ord(digit) - 48)
	
	return ans
# end of decimal


def decimal_subtract(num1:str, num2:str):
	if all([num1.isdigit(), num2.isdigit()]):
		raise ValueError(f"invalid literal with base : '10'")

	max_len = max(len(num1), len(num2))
	num1 = num1.zfill(max_len)
	num2 = num2.zfill(max_len)

	is_negative = False
	if decimal(num1) < decimal(num2):
		num1, num2 = num2, num1
		is_negative = True
		
	ans = []
	borrow = 0
	
	for i in range(max_len - 1, -1, -1):
		dig1 = decimal(num1[i])
		dig2 = decimal(num2[i]) + borrow
		if dig1 >= dig2:
			ans.append(str(dig1 - dig2))
		else:
			ans.append(str(dig1+10 - dig2))
			borrow = 1
	
	ans.reverse()

	ans_str = ''.join(ans).lstrip('0')

	if ans_str == '':
		ans_str = '0'
	
	if is_negative:
		ans_str = '-' + ans_str
	
	return ans_str
# end of decimal_subtract

	
def dec_subtract(num1:str, num2:str) -> int:
	dec_num1 = decimal(num1)
	dec_num2 = decimal(num2)
	
	return dec_num1 + (~dec_num2 + 1)
# end of dec_subtract

#__main__
print(decimal_subtract("0", "1"))
print(decimal_subtract("1", "0"))
print(decimal_subtract("123", "321"))
print(decimal_subtract("888", "999"))
print(decimal_subtract("12345", "321"))
print(decimal_subtract("888", "99999"))
print(decimal_subtract("899", "998"))
print(decimal_subtract("1000", "22"))
print
print(f"1234 - 567 = {decimal_subtract('1234', '567')}")  # Outputs: '667'
print(f"567 - 1234 = {decimal_subtract('567', '1234')}")  # Outputs: '-667'
print(f"1000 - 1000 = {decimal_subtract('1000', '1000')}")  # Outputs: '0'
print(f"2000 - 123 = {decimal_subtract('2000', '123')}")  # Outputs: '1877'
print(f"123 - 2000 = {decimal_subtract('123', '2000')}")  # Outputs: '-1877'
print(f"1000 - 22 = {decimal_subtract('1000', '22')}")  # Outputs: '2'
print(f"0001 - 0001 = {decimal_subtract('0001', '0001')}")  # Outputs: '0'




