class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            isSub = False
            for j in range(len(words)):
                if i!=j and words[i] in words[j]:
                    isSub = True
                    break
            if isSub:
                ans.append(words[i])

        return ans
                
        