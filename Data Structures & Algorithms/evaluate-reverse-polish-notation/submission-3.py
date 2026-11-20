class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*", "/"}
        def oper(n1 ,n2, sign) :
            if n2 == 0 :
                if sign == "*" :
                    return 0
                else :
                    return n1
            else :
                dico = {"+" : n1+n2, "-" : n1-n2, "/" : int(n1/n2), "*" : n1*n2}
                return dico[sign]
        n = len(tokens)
        stack = []
        i = 0
        while  i < n:
            if tokens[i] in op :
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(oper(float(n1),float(n2),tokens[i]))
            else :
                stack.append(tokens[i])
            i+=1
        return int(stack.pop())