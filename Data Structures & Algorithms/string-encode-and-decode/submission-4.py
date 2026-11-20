class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [] :
            return "0"
        encoded_string = ""
        for elt in strs :
            encoded_string = encoded_string + str(len(elt)) + "#" + elt
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if s == "0" :
            return []
        i = 0
        decoded_strs = []
        ens = set("1234567890")
        nb = ""
        while i < len(s) :
            if s[i] in ens :
                nb += s[i]
                i+=1
            elif s[i] == "#" :
                long = int(nb)
                mot = ""
                for j in range(i+1, long+i+1) :
                    mot += s[j]
                decoded_strs.append(mot)
                i = i+1+long
                nb = ""
        return decoded_strs
                    
                

