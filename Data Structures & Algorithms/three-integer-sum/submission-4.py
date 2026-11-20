class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        sol = []
        ens = set()
        for i in range(1,n-1):
            target = -nums[i]
            left, right =  0,  n-1
            while left < i < right :
                total = nums[left] + nums[right]
                if total < target :
                    left+=1
                elif total > target :
                    right-=1
                else :
                    cdd = (nums[left],nums[i],nums[right])
                    if cdd not in ens :
                        sol.append(list(cdd))
                        ens.add(cdd)
                    left+=1
                    right-=1

        return sol


                
                

                
                


