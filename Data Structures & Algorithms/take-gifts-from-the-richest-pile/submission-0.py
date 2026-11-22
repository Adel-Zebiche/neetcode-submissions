import numpy as np
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        def maxi(liste) :
            maxi = (0, liste[0])
            for i, elt in enumerate(liste) :
                if elt > maxi[1] :
                    maxi = (i, elt)
            
            return maxi

        for _ in range(k) :
            idx, maxo = maxi(gifts)
            gifts[idx] = int(np.sqrt(maxo))
        return sum(gifts)
        
        

        
