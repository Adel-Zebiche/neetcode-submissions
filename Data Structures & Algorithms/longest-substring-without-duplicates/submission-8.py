class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dico = {}
        start, maxi = 0, 0
        for i, letter in enumerate(s) :
            if letter in dico and dico[letter] >= start:
                    maxi = max(i-start, maxi)
                    start = dico[letter] + 1
            dico[letter] = i
        return max(maxi, len(s)-start)
                

