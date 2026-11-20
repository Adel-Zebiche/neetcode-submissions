class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dico = defaultdict(int)
        buckets = [[] for _ in range(n+1)] 
        for num in nums :
            dico[num]+=1
        for key, v in dico.items() :
            buckets[v].append(key)
        cpt = 0
        i = n
        output = []
        while cpt < k :
            if buckets[i] != [] :
                cpt+=1
                output.append(buckets[i].pop())
            else :
                i-=1
        return output

