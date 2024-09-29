class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] == words[j][::-1]:
                    cnt+=1
        return cnt