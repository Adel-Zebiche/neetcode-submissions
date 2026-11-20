class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = [c.lower() for c in s if c.isalnum()]
        n = len(word)
        return word == word[::-1]