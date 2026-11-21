class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dico = defaultdict(int)

        for num in nums :
            dico[num]+=1
            if dico[num] > int(len(nums)/2) :
                return num

