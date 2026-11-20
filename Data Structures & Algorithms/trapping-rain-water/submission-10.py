class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        total = 0
        h_l, h_r = 0, 0
        while left < right :
            h_l, h_r = max(h_l,height[left]), max(h_r,height[right])
            if h_l < h_r :
                left+=1
                mini = h_l
                if height[left] < mini :
                    total= total+ mini -height[left]
            else :
                right-=1
                mini = h_r
                if height[right] < mini :
                    total= total+ mini -height[right]
        return total