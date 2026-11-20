class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        dico_ori = Counter(s1)
        dico = dico_ori.copy()
        start, som = 0, 0
        for i, elt in enumerate(s2) :
            if elt in dico :
                if dico[elt] > 0 :
                    dico[elt]-=1
                    som+=1
                    if som == n1 :
                        return True
                else :
                    while s2[start]!=elt :
                        dico[s2[start]]+=1
                        start+=1
                        som-=1
                    start+=1
            else :
                start = i+1
                dico = Counter(s1)
                som = 0
        return False
            



