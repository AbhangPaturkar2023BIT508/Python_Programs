class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {'(':')', '{':'}', '[':']', '<':'>'}

        for bracket in s:
            if bracket in braces:
                stack.append(bracket) 
            elif len(stack)== 0 or bracket != braces[stack.pop()]:
                return False

        return len(stack) == 0