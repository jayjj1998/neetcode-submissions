class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for letter in s:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1
        
        for letter in t:
            if letter in dict1:
                dict1[letter] -= 1
                if dict1[letter] == 0:
                    dict1.pop(letter)
            else:
                return False
        
        return dict1 == { }
            