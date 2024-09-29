class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                xor^=nums[i]
        return xor