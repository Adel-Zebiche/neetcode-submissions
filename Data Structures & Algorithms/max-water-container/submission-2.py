class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxi = 0
        while left < right :
            maxi = max(maxi,min(heights[right], heights[left])* (right-left))
            if heights[right] > heights[left] :
                left+=1
            else :
                right-=1
        return maxi
            
