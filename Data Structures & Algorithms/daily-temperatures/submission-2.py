class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], len(temperatures)*[0]
    
        for i,t in enumerate(temperatures) :
            while stack and temperatures[stack[-1]] < t :
                r = stack.pop()
                output[r] = i-r
            stack.append(i)
        return output


