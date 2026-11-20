class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = []
        for i in range(0,n):
            left, right = i+1, n-1
            target = -nums[i]
            if i > 0 and nums[i] == nums[i-1] :
                    continue
            while left < right :
                total = nums[right] + nums[left] + nums[i]
                if total < 0 :
                    left+=1
                elif total > 0 :
                    right-=1
                else :
                    sol.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left+1 < n and nums[left]== nums[left-1] :
                        left+=1
        return sol


                
                

                
                



