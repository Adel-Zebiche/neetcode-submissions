class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        i = 0
        ref = strs[0]
        n = len(ref)
        while True :
            for mot in strs :
                if n == i or len(mot) == i :
                    return s
                letter = strs[0][i]
                if letter != mot[i] :
                    return s
            s+=letter
            i+=1
