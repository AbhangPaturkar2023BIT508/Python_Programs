class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 0

        for i in range(n, 0, -1):
            if n % i == 0:
                cnt+=1
            
            if cnt > 3:
                return False

        return True if cnt == 3 else False
        