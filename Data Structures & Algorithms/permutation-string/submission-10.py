class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()
        start = 0
        for i, elt in enumerate(s2) :
            window[elt]+=1
            while window[elt] > need[elt] :
                window[s2[start]]-=1
                start+=1

            if i-start+1 == len(s1) :
                return True
            
        return False