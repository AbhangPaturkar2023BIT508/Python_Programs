class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        length = num.bit_length()
        mask = (1 << length) - 1
        return num ^ mask