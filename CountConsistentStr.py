class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            is_consistent = True
            for ch in word:
                if ch not in allowed:
                    is_consistent = False
            if is_consistent:
                count+=1
        return count
        