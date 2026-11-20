class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, maxi = 0, 0
        dico = defaultdict(int)
        for i, letter in enumerate(s) :
            dico[letter]+=1
            
            while sum(dico.values()) - max(dico.values()) > k :
                dico[s[start]] -= 1
                start+=1
            maxi = max(maxi, i-start+1)
        return max(maxi, len(s)-start)


                