class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i in range(0, len(s)-1):
            a += abs(ord(s[i]) - ord(s[i+1]))
        return a