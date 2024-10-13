class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = 0

        for i in range(len(words)-1):
            wordSet = set(words[i])
            for j in range(i+1, len(words)):
                if wordSet == set(words[j]):
                    cnt += 1
        return cnt