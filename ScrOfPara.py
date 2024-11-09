class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        scr = 0
        n = len(s)

        for ch in s:
            if ch is '(':
                stk.append(scr)
                scr = 0
            else:
                scr = stk.pop() + max(2*scr, 1)
        return scr

                    
        