class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        mid = -1

        while start <= end:
            mid = (start + end) // 2

            if mid * mid > x:
                end = mid - 1
            elif mid * mid == x:
                # return int(mid)
                return mid
            else:
                start = mid + 1
            
        # return int(floor(end))
        return end
