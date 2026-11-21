class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        i = 0
        while True :
            for mot in strs :
                if len(strs[0]) == i or len(mot) == i :
                    return s
                elif strs[0][i] != mot[i] :
                    return s
            s+=strs[0][i]
            i+=1
