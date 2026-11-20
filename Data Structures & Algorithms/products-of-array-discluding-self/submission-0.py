class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        prefix, suffix = [1], [1]
        pref, suff = 1, 1
        for i in range(n-1) :
            pref*=nums[i]
            suff*=nums[n-1-i]
            prefix.append(pref)
            suffix.append(suff)
        suffix = [suffix[i] for i in range(n-1,-1,-1)]
        return [prefix[i]*suffix[i] for i in range(n)]

