class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        num = 0
        for i in range(len(nums)):
            num = (num * 2 + nums[i]) % 5
            ans.append(num is 0)
        return ans