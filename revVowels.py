class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        i , j = 0, len(s)-1
        while i <= j:
            if  a[i] not in "aeiouAEIOU":
                i+=1
            elif a[j] not in "aeiouAEIOU":
                j-=1
            else:
                a[i], a[j] = a[j], a[i]
                i+=1
                j-=1
        return ''.join(a)

            