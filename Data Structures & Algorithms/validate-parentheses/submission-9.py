class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #opening = ['{', '[', '(']
        dico = { '{' : '}', '[' : ']', '(' : ')'}
        for elt in s :
            if elt in dico :
                stack.append(elt)
            else :
                if not stack or dico[stack.pop()] != elt :
                    return False
        return not stack


