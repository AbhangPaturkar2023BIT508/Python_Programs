class Solution:
    def get_next_char(self, str1Char: str) -> str:
        return "a" if str1Char == "z" else chr(ord(str1Char) + 1)

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or self.get_next_char(str1[i]) == str2[j]:
                i+=1
                j+=1
            else:
                i+=1

        return True if j == len(str2) else False
            

        