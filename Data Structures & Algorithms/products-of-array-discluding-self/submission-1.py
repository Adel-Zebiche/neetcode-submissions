class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1], [1]
        for i in range(n-1) :
            prefix.append(nums[i]*prefix[i])
            suffix.append(suffix[i]*nums[n-1-i])
        suffix = [suffix[i] for i in range(n-1,-1,-1)]
        return [prefix[i]*suffix[i] for i in range(n)]

