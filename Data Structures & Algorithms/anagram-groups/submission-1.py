class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = {}
        for st in strs :
            tp_str_sort = tuple(sorted(st))
            if tp_str_sort in dico :
                dico[tp_str_sort].append(st)
            else :
                dico[tp_str_sort] = [st]
        
        return [v for v in dico.values()]

            

