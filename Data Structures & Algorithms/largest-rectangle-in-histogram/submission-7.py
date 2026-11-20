class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack, best = [], 0
        
        for i, h in enumerate(heights + [0]) :
            while stack and h <= heights[stack[-1]] :
                hauteur = heights[stack.pop()]
                left, right = 1+stack[-1] if stack else 0, i-1
                best = max(best, (right-left+1)*hauteur)
            stack.append(i)
     
        return best
        
        
            




