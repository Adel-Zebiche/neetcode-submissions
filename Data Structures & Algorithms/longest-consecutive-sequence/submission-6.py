class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_ens= set(nums)
        maxi = 0
        for elt in num_ens :
            if elt-1 not in num_ens :
                score = 1
                while elt + score in num_ens :
                    score+=1
                maxi = max(score, maxi)
        return maxi




            
            
