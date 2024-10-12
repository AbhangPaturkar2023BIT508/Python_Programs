class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        maxi = 0
        for i in range(n):
            if citations[i] >= n-i:
                maxi = max(maxi, n-i)
        return maxi