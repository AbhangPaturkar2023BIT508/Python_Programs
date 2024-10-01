class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        d = list(d.values())

        for i in d:
            if i != (sum(d)//len(d)):
                return False
        return True