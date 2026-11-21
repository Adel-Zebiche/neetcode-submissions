class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dico = defaultdict(int)
        for elt in nums :
            dico[elt]+=1
        i = 0
        while i < dico[0] :
            nums[i] = 0
            i+=1
        while i < dico[0]+dico[1] :
            nums[i] = 1
            i+=1
        while i < len(nums) :
            nums[i] = 2
            i+=1
        