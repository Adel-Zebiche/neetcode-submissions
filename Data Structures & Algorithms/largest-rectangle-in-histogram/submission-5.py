class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights
        n = len(heights)
     
        dico = {}
        stack = []
        
        for i in range(n) :
            while stack and h[i] <= h[stack[-1]] :
                elt = stack.pop()
                dico[elt] = (stack[-1]+1  if stack else 0, i-1) 
            stack.append(i)
        while stack :
            elt = stack.pop()
            dico[elt] = (stack[-1]+1 if stack else 0, n-1)
            
        best = 0
        for i in range(n) :
            area = ((dico[i][1]-dico[i][0])+1)*h[i]
            best = max(best, area)
        
        return best
        
        
            




