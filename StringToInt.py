
def myAtoi(s: str) -> int:
    s = s.removeprefix(' ')
    s1 = ''
    sign = -1 if s[0] == '-' else 1
    for i in range(1,len(s)):
        if s[i].isdigit():
            s1 += s[i]
        else:
            break

    # return int(s1)*sign
    # return s1
    return int(s1)*sign

print(myAtoi('-123a'))
print(type(myAtoi('-123')))