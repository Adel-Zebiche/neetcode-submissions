class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        ref = strs[0]
        n = len(ref)
        for i in range(n) :
            for mot in strs :
                if len(mot) == i :
                    return s
                letter = strs[0][i]
                if letter != mot[i] :
                    return s
            s+=letter
        return ref
