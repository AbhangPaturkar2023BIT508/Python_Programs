class Solution:
    def makeFancyString(self, s: str) -> str:

        ch = s[0]
        freq = 1
        ans = s[0]

        for i in range(1, len(s)):
            if s[i] == ch:
                freq += 1
            else:
                ch = s[i]
                freq = 1

            if freq < 3:
                ans += s[i]

        return ans