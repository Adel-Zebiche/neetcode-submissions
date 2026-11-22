import numpy as np
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        def maxi(liste) :
            high = (0, liste[0])
            for i, elt in enumerate(liste) :
                if elt > high[1] :
                    high = (i, elt)
            return high

        for _ in range(k) :
            idx, maxo = maxi(gifts)
            gifts[idx] = int(np.sqrt(maxo))
        return sum(gifts)
        
        

        
