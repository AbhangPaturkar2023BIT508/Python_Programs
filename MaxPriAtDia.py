class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxPri = 0
        n = len(nums)
        for i in range(n):
            val = nums[i][i]
            if val > 1 and not any(val % i == 0 for i in range(2, int(val**0.5) + 1)):
                if maxPri < val:
                    maxPri = val
        
        for i in range(n):
            val = nums[i][n-i-1]
            if val > 1 and not any(val % i == 0 for i in range(2, int(val**0.5) + 1)):
                if maxPri < val:
                    maxPri = val
        return maxPri
        