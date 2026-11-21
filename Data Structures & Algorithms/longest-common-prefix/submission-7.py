class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        n = len(ref)
        for i in range(n) :
            for mot in strs :
                if len(mot) == i or ref[i] != mot[i]:
                    return ref[:i]
        return ref
