class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = s[0:len(s)/2]
        s2 = s[len(s)/2: len(s)]
        vowels = 'aeiouAEIOU'
        c1 =0
        c2 =0

        for i in range(0, len(s1)):
            if s1[i] in vowels:
                c1+=1
            if s2[i] in vowels:
                c2+=1
        return c1 == c2
        