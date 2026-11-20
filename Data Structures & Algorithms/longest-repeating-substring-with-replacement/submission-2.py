class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, maxi = 0, 0
        dico = defaultdict(int)
        score = 0
        for i, letter in enumerate(s) :
            dico[letter]+=1
            som = sum(dico.values()) - max(dico.values())
            if som > k :
                maxi = max(maxi, score)
                dico[s[start]] -= 1
                start+=1   
            else :
                score+=1
            while sum(dico.values()) - max(dico.values()) > k :
                dico[s[start]] -= 1
                start+=1
                score-=1
        return max(maxi, score)


                