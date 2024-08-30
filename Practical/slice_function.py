def slice(obj : object , slicing_parameter : list[int]) -> object:
    list_of_class_for_slice_operation = [str, list, tuple]
    len_slicing_para = len(slicing_parameter)
    len_obj = len(obj)

    #check for all values in slicing para is int or not
    if not all(isinstance(element, int) for element in slicing_parameter):
        raise TypeError("Slicing parameter must be integer")
    
    # check whether slice is applicable for given object or not
    if type(obj) not in list_of_class_for_slice_operation:
        raise TypeError("Slice not applicable for " + str(type(obj)))
    
    # check whether slicing_parameter contain atmost 3 values or not
    if len_slicing_para > 3:
        raise TypeError("List can contain atmost 3 values 'List[start [,stop [, step]' (given "+str(len_slicing_para)+")")
    
    # check if slicing_parameter contain exact 3 values, then 3rd value (i.e. Step) cannot be 0
    if len_slicing_para == 3 and slicing_parameter[2] == 0:
        raise ValueError("Slice step cannot be zero")

    # if not slicing_parameter given then return given object as it is
    if len_slicing_para == 0:
        return obj

    if len_slicing_para == 1:
        start = slicing_parameter[0]
        end = len_obj
        step = 1

    if len_slicing_para == 2:
        start = slicing_parameter[0]
        end = slicing_parameter[1] if len_obj >= slicing_parameter[1] else len_obj
        step = 1
    
    if len_slicing_para == 3:
        start = slicing_parameter[0]
        end = slicing_parameter[1] if len_obj >= slicing_parameter[1] else len_obj
        step = slicing_parameter[2]

    res = []

    for i in range(start, end, step):
        res.append(obj[i])

    if isinstance(obj, str):
        return ''.join(res)
    else:
        return type(obj)(res)