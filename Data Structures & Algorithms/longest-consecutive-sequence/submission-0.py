class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if nums == [] :
            return 0
        best, current = 1, nums[0]
        maxi = 1
        n = len(nums)
        seen = set()
        for i in range(1,n) :
            if nums[i] not in seen :
                seen.add(nums[i])
                if nums[i] == current+1 :
                    best+=1 
                    maxi = max(best, maxi)
                else :
                    best = 1
            
                current = nums[i]
        return maxi
            
            
