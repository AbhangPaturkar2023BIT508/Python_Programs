class Solution:
    def isPrefixAndSuffix(self, str1 : str, str2 : str) -> bool:
        return str2.startswith(str1) and str2.endswith(str1)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0
        for i in range(0, len(words)-1):
            for j in range(i+1, len(words)):
                # if i is not j:
                cnt += self.isPrefixAndSuffix(words[i], words[j])
        return cnt

