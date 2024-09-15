class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        count = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                count+=1
            if count == 3:
                return nums[i]
        return nums[0]
            
        