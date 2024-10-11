class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*(n+1)

        for val in nums:
            ans[val] = 1

        ans = [i for i in range(1, n+1) if ans[i]==0]
        return ans