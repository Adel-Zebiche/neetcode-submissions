class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cdd1, cdd2 = None, None
        count1, count2 = 0, 0
        for x in nums :
            if x == cdd1 :
                count1+=1
            elif x == cdd2 :
                count2+=1
            elif count1 == 0 :
                cdd1, count1 = x, 1
            elif count2 == 0 :
                cdd2, count2 = x, 1
            else :
                count1-=1
                count2-=1
        
        output = []
        for c in (cdd1, cdd2) :
            if c is not None and nums.count(c) > len(nums) // 3 :
                output.append(c)
        return output