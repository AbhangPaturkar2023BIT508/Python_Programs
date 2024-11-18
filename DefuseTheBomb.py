class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0]*n

        if k == 0:
            return ans

        start = 1
        end = k
        sum = 0
        
        if k < 0:
            start = n - (k*-1)
            end = n - 1
        
        for i in range(start, end+1):
            sum += code[i]

        for i in range(n):
            ans[i] = sum
            sum -= code[start%n]
            sum += code[(end+1)%n]
            start += 1
            end += 1

        return ans

        