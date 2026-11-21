class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1,n) :
            j = i 
            while nums[j] < nums[j-1] and j >=1 :
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
        return nums

