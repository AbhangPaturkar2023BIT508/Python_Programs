class Solution:
    def isValid(self, word: str) -> bool:
        al = 'abcdefghijklmnopqrstuvwxyz'
        l, u = False, False
        c, v = False, False
        d = False
        for i in word:
            if i.isupper():
                if i.lower() in 'aeiou':
                    v = True
                elif i.lower() in al:
                    c = True
                u = True
            elif i.islower():
                if i in 'aeiou':
                    v = True
                elif i in al:
                    c = True
                l = True
            elif i.isdigit():
                d = True
            else:
                return False
        an = int(u) + int(l) + int(d)
        return len(word) >= 3 and an > 0 and c and v