class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                if (nums[j]+nums[j+1]) == (nums[i]+nums[i+1]):
                    cnt+=1
            
        return cnt>=1
        