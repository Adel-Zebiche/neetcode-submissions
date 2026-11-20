class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dico = defaultdict(int)
        for num in nums :
            dico[num] +=1
        L = [(k,v) for k,v in dico.items()]
        L.sort(key = lambda x : x[1], reverse = True)
        return [L[i][0] for i in range(k)]

