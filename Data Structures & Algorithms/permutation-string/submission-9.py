class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dico_ori = Counter(s1)
        dico = dico_ori.copy()
        start = 0
        for i, elt in enumerate(s2) :
            if elt in dico :
                if dico[elt] > 0 :
                    dico[elt]-=1
                    if i-start+1 == len(s1) :
                        return True
                else :
                    while s2[start]!=elt :
                        dico[s2[start]]+=1
                        start+=1
                    start+=1
            else :
                start = i+1
                dico = dico_ori.copy()
        return False
            



