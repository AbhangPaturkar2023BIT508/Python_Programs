
def convert_to_capital_case(text):
	cap_text = ''
	for letter in text:
		unicode_val = ord(letter)
		if unicode_val >= 97 and unicode_val <= 122:
			cap_text += chr(unicode_val - 32)
		else:
			cap_text += letter
	return cap_text
# end of convert_to_capital_case

def convert_to_small_case(text):
	small_text = ''
	for letter in text:
		unicode_val = ord(letter)
		if unicode_val >= 65 and unicode_val <= 90:
			small_text += chr(unicode_val + 32)
		else:
			small_text += letter
	return small_text
# end of convert_to_small_case

def convert_to_reverse_case(text):
	rev_text = ''
	for letter in text:
		unicode_val = ord(letter)
		if unicode_val >= 65 and unicode_val <= 90:
			#rev_text += chr(unicode_val + 32)
			rev_text += convert_to_small_case(letter)
		elif unicode_val >= 97 and unicode_val <= 122:
			#rev_text += chr(unicode_val - 32)
			rev_text += convert_to_capital_case(letter)
		else:
			rev_text += letter
	return rev_text
# end of convert_to_reverse_case

def convert_to_zigzag_case(text):
	zigzag_text = ''
	flag = ord(text[0]) in range(65, 91)
	for letter in text:
		if flag:
			zigzag_text += convert_to_capital_case(letter)
			flag = not flag
		elif not flag:
			zigzag_text += convert_to_small_case(letter)
			flag = not flag
		else:
			zigzag_text += letter
	return zigzag_text
# end of convert_to_zigzag_case

def change_case(text, style):
	if not style:
		return "Invalid Style : function takes only 'C', 'S', 'R', 'Z' (Not Case-sensitive)"
	
	unicode_val = ord(style)
	if unicode_val == 67 or unicode_val == 99:
		return convert_to_capital_case(text)
	elif unicode_val == 83 or unicode_val == 115:
		return convert_to_small_case(text)
	elif unicode_val == 82 or unicode_val == 114:
		return convert_to_reverse_case(text)
	elif unicode_val == 90 or unicode_val == 122:
		return convert_to_zigzag_case(text)
	else:
		return "Invalid Style : function takes only 'C', 'S', 'R', 'Z' (Not Case-sensitive)"		
	#return text + style
# end of change_case
	
#__main__
print(change_case('SggSieT_','C'))
print(change_case('SggSieT_','c'))
print(change_case('SggSieT_','S'))
print(change_case('SggSieT_','s'))
print(change_case('SggSieT_','R'))
print(change_case('SggSieT_','r'))
print(change_case('Sgg_s_','Z'))
print(change_case('sgg_s_','z'))
print(change_case('',''))
# end of __main__
