class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dico_t_ori, dico = Counter(t), defaultdict(int)
        left = 0
        start, end = 0, len(s)+1
        cpt = 0
        for right, letter in enumerate(s) :

            if letter in dico_t_ori :
                if dico[letter] < dico_t_ori[letter] :
                    cpt+=1  
                dico[letter] += 1
            while cpt == len(t) :
                if (right-left+1) < (end-start+1) :
                    start, end = left, right
                letter_left = s[left]
                if letter_left in dico_t_ori :
                    if dico[letter_left] == dico_t_ori[letter_left] :
                        cpt-=1
                    dico[letter_left]-=1
                left+=1
            
        return "" if (start,end) == (0, len(s)+1) else s[start:end+1]
                
            
            
            
                