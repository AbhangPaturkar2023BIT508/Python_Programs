class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)                        
        chSet = [set(words[i]) for i in range(n)]                                                
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (chSet[i] & chSet[j]):
                    max_val=max(max_val, len(words[i]) * len(words[j]))
        
        return max_val   