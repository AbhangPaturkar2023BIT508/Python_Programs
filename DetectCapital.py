class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return any([word == word.upper(), word==word.lower(), word == word.capitalize()])