class Solution:
    def minLength(self, s: str) -> int:
        l = ['AB', 'CD']
        while True:
            if l[0] in s:
                s = s.replace(l[0], '')
            elif l[1] in s:
                s = s.replace(l[1], '')
            else:
                break
        return len(s)