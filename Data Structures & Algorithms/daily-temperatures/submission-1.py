class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack, output = [], n*[0]
    
        for i in range(n) :
            while stack and temperatures[stack[-1]] < temperatures[i] :
                r = stack.pop()
                output[r] = i-r
            stack.append(i)
        return output


