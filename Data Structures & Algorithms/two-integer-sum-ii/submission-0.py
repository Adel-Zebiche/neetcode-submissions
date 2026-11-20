class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        fs, ls = 0, n-1
        while fs < ls :
            som = numbers[fs] + numbers[ls]
            if som > target :
                ls-=1
            elif som < target :
                fs+=1
            else :
                return [fs+1, ls+1]