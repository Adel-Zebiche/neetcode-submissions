class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights
        n = len(heights)
        best = 0
        dico_right, dico_left = {}, {}
        for i in range(n) :
            dico_right[i], dico_left[i] = n, -1
        stack_right, stack_left= [], []
        
        for i in range(n) :
            while stack_right and h[i] < h[stack_right[-1]] :
                dico_right[stack_right.pop()] = i
            stack_right.append(i)
            j = n-1-i
            while stack_left and h[j] < h[stack_left[-1]] :
                dico_left[stack_left.pop()] = j
            stack_left.append(j)
        best = 0
        for i in range(n) :
            area = ((dico_right[i]-dico_left[i])-1)*h[i]
            best = max(best, area)
        
        return best
        
        
            




