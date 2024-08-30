def string_count(main_string, sub_string, allow_overlap = False):
    # print(main_string + sub_string + str(allow_overlap))
    start = 0
    count = 0

    while True:
        start = main_string.find(sub_string, start)

        if start == -1:
            break

        count += 1

        if allow_overlap:
            start += 1
        else:
            start += len(sub_string)
        
    return count
#end of string_count funtion

#__main__
a = 'aaaaaa'
b = 'aa'
print(string_count(a,b,False))
