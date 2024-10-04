class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                ans.append(nums[i])
                if len(ans) == 2:
                    break
        
        return ans