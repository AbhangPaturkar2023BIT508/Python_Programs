class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        n = len(nums)
        bitMask = (2**maximumBit)-1
        xor = 0
        for num in nums:
            xor ^= num

        for i in range(n):
            ans.append(abs(bitMask-xor))
            xor ^= nums.pop()
        
        return ans

        