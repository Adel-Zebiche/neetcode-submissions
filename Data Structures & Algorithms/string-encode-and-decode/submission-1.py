class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for elt in strs :
            encoded_string = encoded_string + elt +"€"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        mot, decoded_strs = "", []
        for elt in s :
            if elt == "€" :
                decoded_strs.append(mot)
                mot = ""
            else :
                mot+=elt
        return decoded_strs
                

