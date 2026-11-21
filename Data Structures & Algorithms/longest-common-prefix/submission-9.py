class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        for i, c in enumerate(strs[0]) :
            for word in strs :
                if len(word) == i or c != word[i]:
                    return ref[:i]
        return ref
