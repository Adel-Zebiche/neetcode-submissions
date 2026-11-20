class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for i in range (len(nums)) :
            g = target - nums[i]
            if g in dico :
                return [dico[g], i]
            
            dico[nums[i]] = i

 
            