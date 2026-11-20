import numpy as np
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = int(max(piles)*np.ceil(len(piles)/h))
        l, r = 1, maxi
        mini = maxi
        while l<=r :
            mid = (l+r) // 2
            total = sum([np.ceil(elt/mid) for elt in piles])
            if total <= h :
                mini = min(mini, mid)
                r = mid+-1
            else :
                l = mid+1
        return mini


