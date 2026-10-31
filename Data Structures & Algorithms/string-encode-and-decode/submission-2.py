class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append("#")
            res.append(word)
        return "".join(res)
        
    def decode(self, encoded_str: str) -> List[str]:
        decoded_words = []
        i = 0
        while i < len(encoded_str):
            #we set a second pointer, the one that finds the pound
            j = i 
            while encoded_str[j] != "#":
                j += 1
            lenght = int(encoded_str[i:j]) #lenght of tsring 
            i = j + 1 #first characted of string
            j = i + lenght
            decoded_words.append(encoded_str[i:j])
            i = j
        return decoded_words
                        





