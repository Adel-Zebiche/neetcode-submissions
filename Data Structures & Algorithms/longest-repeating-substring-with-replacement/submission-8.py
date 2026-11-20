class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, maxi, maxf  = 0, 0, 0
        dico = defaultdict(int)
        for i, letter in enumerate(s) :
            dico[letter]+=1
            maxf = max(maxf, dico[letter])
            while i-start+1 - maxf > k :
                dico[s[start]] -= 1
                start+=1
            maxi = max(maxi, i-start+1)
        return maxi


                