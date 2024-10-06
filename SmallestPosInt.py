class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        ar = [0]*n

        for val in nums:
            if val <= n and val > 0:
                ar[val-1] = 1
        
        for i in range(n):
            if ar[i]==0:
                return i+1

        return n+1

