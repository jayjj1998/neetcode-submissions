class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        all_chars = {}
        for char in s1:
            all_chars[char] = all_chars.get(char, 0) + 1
        
        L = 0
        len_s1 = len(s1)
        for R in range(len(s2)):
            if s2[R] in all_chars:
                all_chars[s2[R]] -= 1
            
            if (R - L + 1) > len_s1:
                if s2[L] in all_chars:
                    all_chars[s2[L]] += 1
                L += 1
            
            print(all_chars)
            if all(value == 0 for value in all_chars.values()):
                return True
        
        return False
