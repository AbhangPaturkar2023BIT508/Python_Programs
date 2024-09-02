class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalkSum = sum(chalk)
        k = k % chalkSum
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            else:
                k -= chalk[i]

        return 0