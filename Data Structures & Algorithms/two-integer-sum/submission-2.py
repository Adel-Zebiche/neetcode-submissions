class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = {}
        for i in range (len(nums)) :
            if (target - nums[i]) not in dico :
                dico[target-nums[i]] = i
        for j in range (len(nums)) :
            if nums[j] in dico and j != dico[nums[j]] :
                i = dico[nums[j]]
                return [min(i,j), max(i,j)]
        
            