class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for elt in nums :
            if elt in seen :
                return elt
            seen.add(elt)