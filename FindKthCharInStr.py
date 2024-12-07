class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        def getNextStr(word):
            ans = ""

            for ch in word:
                nextCh = 'a' if ch == 'z' else chr(ord(ch)+1)
                ans += nextCh
            return ans

        while len(word) < k:
            word += getNextStr(word)
        
        return word[k-1]
        