class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(str)
        b = [10]
        for i in range(0, n):
            b.append(str.count('b',0, i) + str.count('a',i+1, n))

        return min(b)