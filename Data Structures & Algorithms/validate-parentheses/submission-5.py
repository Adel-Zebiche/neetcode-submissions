class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{', '[', '(']
        dico = { '{' : '}', '[' : ']', '(' : ')'}
        for elt in s :
            if elt in opening :
                stack.append(elt)
            else :
                if not stack :
                    return False
                elif dico[stack[-1]] == elt :
                    stack.pop()
                else :
                    return False
        return len(stack) == 0


