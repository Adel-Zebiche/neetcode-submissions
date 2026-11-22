class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        dico = defaultdict(int)
        for elt in nums :
            dico[elt] += 1
            if dico[elt] == int(n/3)+1  :
                output.append(elt)
        return output
                
                