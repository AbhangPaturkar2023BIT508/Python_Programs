def get_sum(nums : list) -> int:
    ans = 0
    for i in nums:
        if type(i) in (list, tuple):
            ans += get_sum(list(i))
        if isinstance(i, (int, float, complex)):
            ans += i

    return ans

print(get_sum([1,2,3,[1,2,3,(1,2,3,[1,2,3])]]))
    