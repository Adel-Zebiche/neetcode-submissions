class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening, closing = ['{', '[', '('], ['}', ']', ')']
        dico = { '{' : '}', '[' : ']', '(' : ')'}
        cpt_open = 0
        for elt in s :
            if elt in opening :
                stack.append(elt)
                cpt_open +=1
            else :
                if cpt_open == 0 :
                    return False
                elif dico[stack[-1]] == elt :
                    stack.pop()
                    cpt_open-=1
                else :
                    return False
        return cpt_open == 0


