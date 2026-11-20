class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxi = min(heights[right], heights[left])* (right-left)
        while left < right :
            if heights[right] > heights[left] :
                left+=1
            elif heights[right] < heights[left] :
                right-=1
            else :
                left+=1
                right-=1
            cdd = min(heights[right], heights[left]) * (right-left)
            maxi = max(maxi, cdd)
        
        return maxi
            
