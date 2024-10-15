class Solution:
    def minimumSteps(self, s: str) -> int:
        s = s.rstrip('1')
        s = s.lstrip('0')
        i, j = 0, 0
        n = len(s)
        cnt = 0

        while j < n:
            if s[j] == '1':
                j+=1
            else:
                cnt += j - i
                i+=1
                j+=1

        return cnt