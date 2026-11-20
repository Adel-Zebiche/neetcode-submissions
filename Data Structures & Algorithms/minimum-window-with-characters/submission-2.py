class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n_s = len(s)
        set_t = set(t)
        dico_t_ori, dico = Counter(t), defaultdict(int)
        left, right = 0, 0
        start, end = 0, n_s+1
        cpt = 0
        while True :
            if cpt == len(t) :
                if right-left < end-start :
                    start, end = left, right
                letter_left = s[left]
                if letter_left in set_t :
                    if dico[letter_left] == dico_t_ori[letter_left] :
                        cpt-=1
                    dico[letter_left]-=1
                left+=1
            else :
                if right == n_s :
                    if (start,end) == (0, n_s+1) :
                        return ""
                    else :
                        return s[start:end]
                else :
                    letter = s[right]
                    if letter in set_t :
                        if dico[letter] < dico_t_ori[letter] :
                            cpt+=1  
                        dico[letter] += 1
                    right+=1
            
            
            
                