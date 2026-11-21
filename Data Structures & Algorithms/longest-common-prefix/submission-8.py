class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        for i in range(len(ref)) :
            for mot in strs :
                if len(mot) == i or ref[i] != mot[i]:
                    return ref[:i]
        return ref
