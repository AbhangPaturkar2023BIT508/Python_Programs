class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len = max(len(num1), len(num2))
        num1 = num1.zfill(max_len)
        num2 = num2.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            dig1 = ord(num1[i]) - ord('0') 
            dig2 = ord(num2[i]) - ord('0') 
            
            total = dig1 + dig2 + carry
            result.append(str(total % 10)) 
            carry = total // 10 

        if carry:
            result.append(str(carry))

        result.reverse()
        return ''.join(result)
