class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        liste = [(position[i], speed[i]) for i in range(len(position))]
        liste.sort(key = lambda x : x[0])
        stack = []
        cpt = 0
        for position, speed in liste :
            h = ((target-position)/speed)
            stack.append(h)
        elt = stack.pop()
        cpt = 1
        while stack :
            if elt < stack[-1] :
                elt = stack.pop()
                cpt+=1      
            else :
                stack.pop()
          
        return cpt
        




        

                
                    




