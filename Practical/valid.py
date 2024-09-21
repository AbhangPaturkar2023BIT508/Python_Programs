def check_validity(text : str) -> bool:
    stack = []
    braces = {'(':')', '{':'}', '[':']', '<':'>'}

    for bracket in text:
        if bracket not in '({[<>]})':
            return 'Invalid char'
        elif bracket in braces:
            stack.append(bracket) 
        elif len(stack) == 0 or bracket != braces[stack.pop()]:
            return 'Invalid'

    return 'valid' if len(stack) == 0 else 'Imbalanced count'

def get_valid_invalid_text_count(txt_list : list) -> tuple:
    valid_cnt = 0
    invalid_cnt = 0

    for txt in txt_list:
        if isinstance(txt, str):
            if check_validity(txt) == 'valid':
                valid_cnt+=1
            else:
                invalid_cnt+=1
        elif isinstance(txt, (list, tuple, set)):
                tmp = get_valid_invalid_text_count(list(txt))
                valid_cnt += tmp[0]
                invalid_cnt += tmp[1]
    return valid_cnt, invalid_cnt




# print(check_validity('(a)'))
# print(check_validity('(<)>'))
# print(check_validity('(a)'))
# print(check_validity('+()'))
# print(check_validity(')('))
# print(check_validity(''))
# print(check_validity('(())'))
# print(check_validity('({['))


a = ['[{(', [45,("()"),]]
print(get_valid_invalid_text_count(a))