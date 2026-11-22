class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_Palindrom(w) :
            l, r = 0, len(w)-1
            while l<=r :
                if w[l] != w[r] :
                    return False
                l+=1
                r-=1
            return True
        
        left, right = 0, len(s)-1
        while left <= right :
            if s[left] != s[right] :
               return is_Palindrom(s[left:right]) or is_Palindrom(s[left+1:right+1])
            left+=1
            right-=1       
        return True