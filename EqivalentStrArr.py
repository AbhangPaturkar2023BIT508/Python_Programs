class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        str1 = ""
        str2 = ""
        for word in word1:
            str1+=word
        for word in word2:
            str2+=word

        return str1 == str2
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        
    def arrayStringsAreEqual_1(self, word1, word2):
        return ''.join(word1) == ''.join(word2)
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """