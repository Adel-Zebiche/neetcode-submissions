class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        cpt = 0
        while l <= r :
            g, d = nums[l], nums[r]
            if g == val and d != val :
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            elif g == val :
                r-=1
            elif d != val :
                l+=1
            else :
                l+=1
                r-=1
        return r+1
