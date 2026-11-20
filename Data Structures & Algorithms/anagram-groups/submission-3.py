class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for st in strs :
            tp_str_sort = tuple(sorted(st))
            group[tp_str_sort].append(st)
        
        return [v for v in group.values()]

            

