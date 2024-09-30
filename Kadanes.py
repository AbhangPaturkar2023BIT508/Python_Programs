class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = 0
        ms = nums[0]

        for val in nums:
            cs += val
            ms = max(cs, ms)
            if cs < 0:
                cs = 0
            
        return ms