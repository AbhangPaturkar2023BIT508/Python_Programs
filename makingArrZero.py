class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniqueNum = set()
        for i in nums:
            if i == 0:
                continue
            if i in uniqueNum:
                continue
            uniqueNum.add(i)
        return len(uniqueNum)

        