class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []

        for ch in s:
            if len(stk) != 0 and stk[-1] == '(' and ch is ')':
                stk.pop()
            else:
                stk.append(ch)
            
        return len(stk)

        