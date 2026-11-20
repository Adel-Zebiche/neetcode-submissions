class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_ens = set(nums) 
        dico = defaultdict(int)
        seen = set()
        maxi = 0
        for elt in (num_ens-seen) :
            if elt not in seen :
                seen.add(elt)
                score = 1
                start = elt
                while elt+1 in num_ens :
                    score+=1
                    elt+=1
                    seen.add(elt)
                while start-1 in num_ens :
                    score+=1
                    start-=1
                    seen.add(start)
                maxi = max(maxi, score)
        return maxi




            
            
