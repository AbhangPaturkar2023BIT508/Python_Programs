class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        realMax = 0
        for i in range(len(strs)):
            if strs[i].isdigit():
                realMax = max(realMax, int(strs[i]))
            elif len(strs[i])> realMax:
                realMax = max(realMax, len(strs[i]))
                    
        return realMax
        