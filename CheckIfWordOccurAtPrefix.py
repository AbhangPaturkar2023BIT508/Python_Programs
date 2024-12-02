class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen = sentence.split()
        for i in range(1, len(sen)+1):
            if sen[i-1].startswith(searchWord):
                return i
        
        return -1
        