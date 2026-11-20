class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dico = {}
        for num in nums :
            if num in dico :
                return True
            else :
                dico[num] = 1
        return False
        