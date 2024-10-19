class Solution:
    def invertBit(self, n: str) -> str:
        num = int(n, 2)
        bit_size = len(n)
        mask = (1<<bit_size)-1
        num = num ^ mask
        return bin(num)[2:]
    
    def findKthBit(self, n: int, k: int) -> str:
        dp = ['0']*(n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + '1'+ self.invertBit(dp[i-1])[::-1]

        return dp[n][k-1]
        