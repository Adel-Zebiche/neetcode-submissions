class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        best = 0
        for i in range(n) :
            while stack and heights[i] <= heights[stack[-1]] :
                elt = stack.pop()
                left, right = 1+stack[-1] if stack else 0, i-1
                best = max(best, (right-left+1)*heights[elt])
            stack.append(i)
        while stack :
            elt = stack.pop()
            left, right = 1+stack[-1] if stack else 0, n-1
            best = max(best, (right-left+1)*heights[elt])
            
        return best
        
        
            




