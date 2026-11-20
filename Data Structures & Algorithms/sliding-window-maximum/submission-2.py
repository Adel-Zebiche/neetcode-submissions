class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = []
        for r, val in enumerate(nums) :
            while queue and nums[queue[-1]] < val :
                queue.pop()
            queue.append(r)
            if queue[0] < r-k+1 :
                queue.popleft()
            
            if r >= k-1 :
                output.append(nums[queue[0]])
        
        return output
            


                


