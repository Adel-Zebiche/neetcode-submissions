class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        output = n*[0]
        
        for i in range(n) :
            temp = temperatures[i]
            while stack and temperatures[stack[-1]] < temp :
                r = stack.pop()
                output[r] = i-r
            stack.append(i)
        return output


